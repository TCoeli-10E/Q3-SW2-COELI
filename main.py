from pyscript import document, display

def intram(e):
    document.getElementById("outputall").innerHTML = ""
    document.getElementById("output").innerHTML = ""
    regis = document.querySelector('input[name="regis"]:checked').value
    medi = document.querySelector('input[name="medi"]:checked').value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    if regis == "yes" and medi == "yes" and grade in ["7", "8", "9", "10"]:
        eligible = "Yes"
    else:
        eligible = "You are not eligible for registration."

    eligibility = eligible

    if eligibility == "Yes" and section in ["ruby"]:
        team="Red Team"
    elif eligibility == "Yes" and section in ["sapphire"]:
        team="Blue Team"
    elif eligibility == "Yes" and section in ["emerald"]:
        team="Green Team"
    elif eligibility == "Yes" and section in ["topaz"]:
        team="Yellow Team"
    elif eligibility == "You are not eligible for registration.":
        team="blehh"

    if team == "Red Team":
        display(f'You are assigned to the red bulldogs.', target='output')
        document.getElementById("outputall").innerHTML = "<img src='redy.jpeg' alt='Red Team' height='100' width='100'>"
    elif team == "Blue Team":
        display(f'You are assigned to the blue bears.', target='output')
        document.getElementById("outputall").innerHTML = "<img src='bluey.jpg' alt='Blue Team' height='100' width='100'>"
    elif team == "Green Team":
        display(f'You are assigned to the green hornets.', target='output')
        document.getElementById("outputall").innerHTML = "<img src='greeny.jpeg' alt='Green Team' height='100' width='100'>"  
    elif team == "Yellow Team":
        display(f'You are assigned to the yellow tigers.', target='output')
        document.getElementById("outputall").innerHTML = "<img src='yellowy.jpeg' alt='Yellow Team' height='100' width='100'>"
    elif team == "blehh":
        display(f'You arent registered.', target='output')
            