const API_URL = "https://5h9usbrct6.execute-api.us-east-1.amazonaws.com/chat";

async function sendMessage() {

    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") return;

    // Show user message
    chatBox.innerHTML += `
        <div class="user">
            ${message}
        </div>
    `;

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || `HTTP Error ${response.status}`);
        }

        // Render Markdown
        chatBox.innerHTML += `
            <div class="bot">
                ${marked.parse(result.reply)}
            </div>
        `;

    } catch (error) {

        console.error(error);

        chatBox.innerHTML += `
            <div class="bot">
                ❌ ${error.message}
            </div>
        `;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send button
document.querySelector("button").addEventListener("click", sendMessage);

// Enter key
document.getElementById("message").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }

});
