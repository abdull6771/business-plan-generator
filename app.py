from flask import Flask, request, render_template
import os
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from typing import Dict, TypedDict
import markdown

app = Flask(__name__)

# Set your Groq API Key
os.environ["GROQ_API_KEY"] = "your api key"

# Initialize Llama 3.1 8B for text generation
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

class BusinessPlanState(TypedDict):
    business_idea: str
    market_analysis: str
    business_strategy: str
    financial_projection: str
    investor_pitch: str

def market_analysis_agent(state: BusinessPlanState):
    prompt = ChatPromptTemplate.from_template(
        """You are a business analyst. Analyze the market for the following startup idea,
        including industry trends, customer demand, and key competitors.
        Business Idea: {business_idea}"""
    )
    chain = prompt | llm
    response = chain.invoke({"business_idea": state["business_idea"]}).content
    return {"market_analysis": response}

def business_strategy_agent(state: BusinessPlanState):
    prompt = ChatPromptTemplate.from_template(
        """You are a startup strategy expert. Develop a structured business strategy
        based on market research. Include revenue model, target audience, and growth strategy.
        Market Analysis: {market_analysis}"""
    )
    chain = prompt | llm
    response = chain.invoke({"market_analysis": state["market_analysis"]}).content
    return {"business_strategy": response}

def financial_projection_agent(state: BusinessPlanState):
    prompt = ChatPromptTemplate.from_template(
        """You are a financial analyst. Provide a detailed financial projection for the startup,
        including initial costs, expected revenue, break-even point, and profit forecasts.
        Business Strategy: {business_strategy}"""
    )
    chain = prompt | llm
    response = chain.invoke({"business_strategy": state["business_strategy"]}).content
    return {"financial_projection": response}

def investor_pitch_agent(state: BusinessPlanState):
    prompt = ChatPromptTemplate.from_template(
        """You are an expert in startup pitches. Create a compelling investor pitch based on the
        business plan and financial projections. Focus on market opportunity, revenue model,
        and potential return on investment.
        Financial Projection: {financial_projection}"""
    )
    chain = prompt | llm
    response = chain.invoke({"financial_projection": state["financial_projection"]}).content
    return {"investor_pitch": response}

# Setup LangGraph
graph = StateGraph(BusinessPlanState)
graph.add_node("market_analysis_agent", market_analysis_agent)
graph.add_node("business_strategy_agent", business_strategy_agent)
graph.add_node("financial_projection_agent", financial_projection_agent)
graph.add_node("investor_pitch_agent", investor_pitch_agent)
graph.set_entry_point("market_analysis_agent")
graph.add_edge("market_analysis_agent", "business_strategy_agent")
graph.add_edge("business_strategy_agent", "financial_projection_agent")
graph.add_edge("financial_projection_agent", "investor_pitch_agent")
graph.add_edge("investor_pitch_agent", END)
graph = graph.compile()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        business_idea = request.form['business_idea']
        try:
            result = graph.invoke({"business_idea": business_idea})
            # Convert markdown to HTML
            for key in ['business_strategy', 'financial_projection', 'investor_pitch']:
                result[key] = markdown.markdown(result[key])
        except Exception as e:
            result = {'error': str(e)}
    return render_template('index.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)