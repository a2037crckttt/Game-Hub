<h1>Game Hub – Python Mini Game Launcher</h1>
<p>
Game Hub is a desktop application built using Python and CustomTkinter that acts as a central launcher for multiple mini-games. It provides a modern, dark-themed UI where users can easily select and launch different games from a single window.
Each game runs independently in its own thread, ensuring the main launcher remains responsive while a game is running.
</p>

<h1>Features</h1>
<uL>
<li>Modern GUI built with CustomTkinter</li>
<li>Dark theme with smooth hover effects</li>
<li>Centralized launcher for multiple Python games</li>
<li>Multi-threaded game execution (no UI freezing)</li>
<li>Modular design – easy to add new games</li>
<li>Clean and minimal layout</li>
</uL>

<h1>Included Games</h1>
<p>
<ol>
<li><b>BIHARI F1</b> – Car racing game</li>
<li><b>Rock Paper Scissors</b> – Classic game with GUI</li>
<li><b>Tic Tac Toe</b> – Two-player grid game</li>
<li><b>Space Monkey</b> – Space-themed arcade game</li>
</ol>
</p>

<h1>Technologies Used</h1>
<ul>
<li>Python</li>
<li>CustomTkinter</li>
<li>Threading</li>
<li>Modular Python imports</li>
</ul>

<h1>How It Works</h1>
The main window is created using CTk
<ul>
<li>Each button is linked to a game function</li>
<li>Games are launched in separate threads to avoid blocking the GUI</li>
<li>The project follows a modular folder structure, keeping each game independent</li>
</ul>

<h1>Project Structure (Example)</h1>

```
Game-Hub/
│
├── main.py
├── arav/
│   └── racing_game.py
├── arrham/
│   └── final_rock_paper_scissors.py
├── roshan/
│   └── xox.py
├── krishna/
│   └── code/
│       └── main.py
```

<h1>Installation & Run</h1>

    pip install customtkinter
    python main.py

<h1>Future Improvements</h1>
<ul>
<li>Sound effects and background music</li>
<li>Score tracking and leaderboards</li>
<li>Game previews inside the launcher</li>
<li>Packaging as a standalone .exe</li>
</ul>

<h1>Team</h1>
<p>
Arrham - <a href="">Visit GitHub</a>
Arav - <a href="">Visit GitHub</a>
Roshan - <a href="">Visit GitHub</a>
Krishna - <a href="">Visit GitHub</a>
</p>
