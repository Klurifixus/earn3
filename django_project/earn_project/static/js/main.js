// static/js/main.js
document.addEventListener('DOMContentLoaded', (event) => {
    console.log("The DOM has fully loaded");
    // JavaScript code goes here
});

document.querySelector('button').addEventListener('click', () => {
    alert('Button was clicked!');
});

fetch('/some-endpoint/', {
    method: 'POST', // or 'GET'
    headers: {
        'Content-Type': 'application/json',
        // Include CSRF token header for POST requests
        'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ key: 'value' }) // if POST
})
.then(response => response.json())
.then(data => {
    console.log(data);
})
.catch((error) => {
    console.error('Error:', error);
});

// Function to get cookie by name; needed for CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
