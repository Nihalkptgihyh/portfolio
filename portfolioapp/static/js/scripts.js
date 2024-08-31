function toggleDarkMode() {
    // Toggle the 'dark-mode' class on the body
    document.body.classList.toggle('dark-mode');

    // Change the icon of the dark mode button based on the current mode
    const darkModeToggle = document.querySelector('.dark-mode-toggle i');
    if (document.body.classList.contains('dark-mode')) {
        darkModeToggle.classList.remove('fa-moon');
        darkModeToggle.classList.add('fa-sun');
    } else {
        darkModeToggle.classList.remove('fa-sun');
        darkModeToggle.classList.add('fa-moon');
    }
}
