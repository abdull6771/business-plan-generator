document.querySelector('form').addEventListener('submit', function() {
    const button = document.querySelector('button[type="submit"]');
    button.disabled = true;
    button.innerHTML = 'Generating... <span class="animate-spin inline-block">⌀</span>';
});