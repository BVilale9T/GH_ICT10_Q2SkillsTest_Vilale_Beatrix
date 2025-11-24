from pyscript import document, display

sports_data = {
    "Basketball Club":{
        "desc":"Basketball Club is for players who want to improve their skills and compete.",
        "practice_time":"Tuesdays 5:00-6:30 PM",
        "location":"Gymnasium",
        "coach":"Coach Thompson",
        "num_of_players":"15"
    },
    "Chess Club":{
        "desc":"Chess Club is a place to learn strategies and compete in tournaments.",
        "practice_time":"Thursdays 3:00-4:30 PM",
        "location":"Library Room 3",
        "coach":"Mr. Perez",
        "num_of_players":"12"
    },
    "Photography Club":{
        "desc":"Photography Club explores digital photography techniques and photo editing.",
        "practice_time":"Saturdays 10:00 AM-12:00 PM",
        "location":"Room 204",
        "coach":"Ms. Carter",
        "num_of_players":"22"
    }
}

def display_club_info(e):
    selected_club = document.getElementById("club_select").value
    club_details = sports_data[selected_club]

    document.getElementById("club_output").innerHTML = ""

    display(f"Club: {selected_club}", target="club_output")
    display(f"Description: {club_details['desc']}", target="club_output")
    display(f"Practice Time: {club_details['practice_time']}", target="club_output")
    display(f"Location: {club_details['location']}", target="club_output")
    display(f"Coach: {club_details['coach']}", target="club_output")
    display(f"Number of Players: {club_details['num_of_players']}", target="club_output")
