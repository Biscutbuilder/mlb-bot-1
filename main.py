from datetime import date
from mlbstatsapi import Mlb
import statsapi
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("MLB Game Scores")
window.geometry("600x300")
# above is my code to make the window

# Frame to hold the scores
scores_frame = tk.Frame(window)
scores_frame.pack(padx=20, pady=20)


def update_scores():

    for widget in scores_frame.winfo_children():
        widget.destroy()

    today = date.today().strftime("%Y-%m-%d")

    try:
        with Mlb() as mlb:
            scoring_plays = statsapi.game_scoring_plays(824310)
            schedule = mlb.get_schedule(
                date=today,
                team_id=138
            )

            for date_obj in schedule.dates:
                for game in date_obj.games:
                    away_team = game.teams.away.team.name
                    away_score = game.teams.away.score

                    home_team = game.teams.home.team.name
                    home_score = game.teams.home.score

                    score_label = tk.Label(
                        scores_frame,
                        text=f"{away_team} {away_score} - "
                             f"{home_team} {home_score}",
                        font=("Arial", 16)
                    )
                    recent_play = tk.Label(
                        text=f"Recent Play:\n{'\n'.join(reversed(scoring_plays.splitlines()))}"
                    )
                    recent_play.pack(pady=5)
                    score_label.pack(pady=5)

    except Exception as e:
        error_label = tk.Label(
            scores_frame,
            text=f"Error getting scores: {e}",
            font=("Arial", 12),
            fg="red"
        )
        error_label.pack(pady=5)

    window.after(10_000, update_scores)


update_scores()

window.mainloop()
