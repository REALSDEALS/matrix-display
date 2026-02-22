// Matrix | script.js | REALSDEALS

async function fetchContributions() {
    const username = document.getElementById('usernameInput').value;
    const grid = document.getElementById('grid');
    const nameDisplay = document.getElementById('username-display');
    
    if (!username) return;

    grid.innerHTML = '';
    nameDisplay.innerText = 'loading...';

    try {
        // Call Local Python backend API
        const response = await fetch(`/api/contributions/${username}`);
        const data = await response.json();

        if (data.error) {
            nameDisplay.innerText = 'error fetching user';
            return;
        }

        nameDisplay.innerText = data.username;

        // Create a Pixel Block for each Day:
        data.contributions.forEach(day => {
            const pixel = document.createElement('div');
            pixel.classList.add('pixel');
            pixel.classList.add(`level-${day.level}`);
            pixel.title = day.date; 
            grid.appendChild(pixel);
        });

    } catch (error) {
        console.error("Failed to fetch data:", error);
        nameDisplay.innerText = 'connection error';
    }
}

// Toggle Fullscreen mode for the whole webpage
function toggleFullScreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
            console.log(`Error attempting to enable fullscreen: ${err.message}`);
        });
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// Loading Defaults:
window.onload = fetchContributions;