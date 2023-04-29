const closeBtn = document.getElementById('close');
const box = document.getElementById('alertBox');
const formSend = document.getElementById('form');
const confirmBtn = document.getElementById('confirm');
const input = document.querySelectorAll('.inputField');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    box.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    box.style.display = 'none';
});

confirmBtn.addEventListener('click', () => {
    box.style.display = 'none';
    Array.from(input).forEach(function (item) {
        item.classList.add('disabled');
    });
});