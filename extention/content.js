chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getEmailBody") {
      const emailBody = document.querySelector('.ii.gt').innerHTML;
      sendResponse({ body: emailBody });
    }
  });