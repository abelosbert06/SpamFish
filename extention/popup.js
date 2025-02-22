document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('checkEmailButton').addEventListener('click', function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { action: 'getEmailBody' }, async function (response) {
                if (response) {
                    const emailBody = response.body;
                    const isScam = await checkSpam(emailBody);
                    displayResult(isScam);
                }
            });
        });
    });
});

async function checkSpam(emailBody) {
    const response = await fetch("http://127.0.0.1:8000/check_spam", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: emailBody })
    });
    const result = await response.json();
    return result.is_spam;
}

function displayResult(isScam) {
    const resultDiv = document.getElementById('result');
    if (isScam) {
        resultDiv.textContent = 'This email might be a scam. Be cautious!';
        resultDiv.style.color = 'red';
    } else {
        resultDiv.textContent = 'This email seems safe.';
        resultDiv.style.color = 'green';
    }
}
