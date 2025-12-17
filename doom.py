import customtkinter as ctk
import threading

from arav.racing_game import car_game
from arrham.final_rock_paper_scissors import rock_paper
from roshan import xox
from krishna.code.main import space_game

main_window = ctk.CTk()
main_window.title("Games")
main_window.geometry("900x720")
main_window.configure(fg_color="#000000")

games_frame = ctk.CTkFrame(main_window, fg_color="#141414", corner_radius=20)
games_frame.pack(fill="both", expand=True, padx=20, pady=20)

header = ctk.CTkLabel(
    games_frame,
    text="Pick A Game",
    font=("Agency FB", 30, "bold"),
    text_color="#ffffff"
)
header.pack(pady=20)

btn_style = {
    "corner_radius": 18,
    "height": 110,
    "width": 240,
    "font": ("Agency FB", 20, "bold"),
    "fg_color": "#080707",
    "hover_color": "#0E3C10",
    "text_color": "#ffffff"
}

def launch_game(game_func):
    threading.Thread(
        target=game_func,
        args=(main_window,),
        daemon=True
    ).start()

ctk.CTkButton(
    games_frame,
    text="Game1",
    command=lambda: launch_game(car_game),
    **btn_style
).pack(pady=20)

ctk.CTkButton(
    games_frame,
    text="Game2",
    command=lambda: launch_game(rock_paper),
    **btn_style
).pack(pady=20)

ctk.CTkButton(
    games_frame,
    text="Game3",
    command=lambda: launch_game(xox),
    **btn_style
).pack(pady=20)

ctk.CTkButton(
    games_frame,
    text="Game4",
    command=lambda: launch_game(space_game),
    **btn_style
).pack(pady=20)

main_window.mainloop()
