const verifyBtn = document.getElementById("verifyBtn");
const popup = document.getElementById("aiPopup");
const progressBar = document.getElementById("progressBar");
const progressText = document.getElementById("progressText");
const form = document.getElementById("docForm");
const fileInput = document.querySelector("input[type='file']");
const fileNameText = document.getElementById("file-name");

// Show selected file name
fileInput.addEventListener("change", () => {
    fileNameText.innerText = fileInput.files[0]?.name || "No file selected";
});

verifyBtn.addEventListener("click", () => {

    if (fileInput.files.length === 0) {
        alert("Please upload a document first!");
        return;
    }

    popup.classList.remove("hidden");

    let progress = 0;

    const interval = setInterval(() => {
        progress += 10;
        progressBar.style.width = progress + "%";

        if (progress === 30) progressText.innerText = "Checking clarity & blur...";
        if (progress === 60) progressText.innerText = "Detecting rejection risks...";
        if (progress === 90) progressText.innerText = "Finalizing document...";

        if (progress >= 100) {
            clearInterval(interval);
            progressText.innerText = "Redirecting...";
            setTimeout(() => form.submit(), 500);
        }
    }, 300);
});