const BACKEND_URL = 'http://localhost:5000';
async function loadMessages() {
    try {
        const response = await fetch(`${BACKEND_URL}/messages`);
        if (!response.ok) throw new Error('Network response was not ok');
        const messages = await response.json();
        
        const messagesList = document.getElementById('messagesList');
        messagesList.innerHTML = '';
        
        messages.forEach(msg => {
            const messageElement = document.createElement('div');
            messageElement.className = 'message';
            messageElement.textContent = msg.content;
            messagesList.appendChild(messageElement);
        });
    } catch (error) {
        console.error('Error loading messages:', error);
        alert('Error loading messages. See console for details.');
    }
}

async function sendMessage() {
    const input = document.getElementById('messageInput');
    const content = input.value.trim();
    
    if (content) {
        try {
            const response = await fetch(`${BACKEND_URL}/messages`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ content })
            });
            
            if (!response.ok) throw new Error('Failed to send message');
            
            input.value = '';
            await loadMessages();
        } catch (error) {
            console.error('Error sending message:', error);
            alert('Error sending message. See console for details.');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('button').addEventListener('click', sendMessage);
    
    document.getElementById('messageInput').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    loadMessages();
});