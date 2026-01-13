const fileInput = document.querySelector('input[type="file"]');
const fileName = document.getElementById('file-name');

fileInput.addEventListener('change', function () {
    fileName.textContent = this.files[0].name;
});
