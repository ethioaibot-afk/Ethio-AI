function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    if (input.value.trim() === "") return;

    chatBox.innerHTML += `
        <div class="message user">
            ${input.value}
        </div>
    `;

    chatBox.innerHTML += `
        <div class="message bot">
            I'm Ethio AI. Backend hin qabu amma.
        </div>
    `;

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}
