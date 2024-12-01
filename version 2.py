import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from bs4 import BeautifulSoup

# Attribute mapping dictionary
attribute_mapping = {
    'Wor': 'Work Rate',
    'Vis': 'Vision',
    'Thr': 'Throwing',
    'Tec': 'Technique',
    'Tea': 'Teamwork',
    'Tck': 'Tackling',
    'Str': 'Strength',
    'Sta': 'Stamina',
    'TRO': 'Rushing Out (Tendency)',
    'Ref': 'Reflexes',
    'Pun': 'Punching (Tendency)',
    'Pos': 'Positioning',
    'Pen': 'Penalty Taking',
    'Pas': 'Passing',
    'Pac': 'Pace',
    '1v1': 'One On Ones',
    'OtB': 'Off The Ball',
    'Nat': 'Natural Fitness',
    'Mar': 'Marking',
    'L Th': 'Long Throws',
    'Lon': 'Long Shots',
    'Ldr': 'Leadership',
    'Kic': 'Kicking',
    'Jum': 'Jumping Reach',
    'Hea': 'Heading',
    'Han': 'Handling',
    'Fre': 'Free Kick Taking',
    'Fla': 'Flair',
    'Fir': 'First Touch',
    'Fin': 'Finishing',
    'Ecc': 'Eccentricity',
    'Dri': 'Dribbling',
    'Det': 'Determination',
    'Dec': 'Decision Making',
    'Cro': 'Crossing',
    'Cor': 'Corners',
    'Cnt': 'Concentration',
    'Cmp': 'Composure',
    'Com': 'Communication',
    'Cmd': 'Command Of Area',
    'Bra': 'Bravery',
    'Bal': 'Balance',
    'Ant': 'Anticipation',
    'Agi': 'Agility',
    'Agg': 'Aggression',
    'Aer': 'Aerial Ability',
    'Acc': 'Acceleration'
}

def parse_html_file(file_path):
    """
    Parse the uploaded HTML file and extract player data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    player_data = {}

    # Extract attribute data
    for abbr, full_name in attribute_mapping.items():
        cell = soup.find('th', text=abbr)
        if cell:
            # Find the corresponding value cell
            value = cell.find_next('td').text.strip()
            player_data[full_name] = value

    return player_data

def calculate_min_max(value):
    """
    Parse a value range (e.g., "10-15") into min and max values.
    """
    if '-' in value:
        min_val, max_val = map(int, value.split('-'))
    elif value.isdigit():
        min_val = max_val = int(value)
    else:
        min_val = max_val = 0
    return min_val, max_val

def calculate_scores(player_data, role_attributes):
    """
    Calculate minimum and maximum scores for a role.
    """
    score_min, score_max = 0, 0
    for attribute, role_value in role_attributes.items():
        player_value = player_data.get(attribute, '0')
        role_min, role_max = calculate_min_max(str(role_value))
        player_min, player_max = calculate_min_max(player_value)
        score_min += max(player_min, role_min)
        score_max += min(player_max, role_max)
    return score_min, score_max

def create_interface():
    """
    Create the GUI interface using Tkinter.
    """
    def load_file():
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if not file_path:
            return
        try:
            global player_data
            player_data = parse_html_file(file_path)
            messagebox.showinfo("Success", "File loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def analyze_role():
        selected_role = role_var.get()
        if not selected_role or selected_role not in roles_data:
            messagebox.showwarning("Warning", "Please select a valid role.")
            return

        role_data = roles_data[selected_role]
        min_score, max_score = calculate_scores(player_data, role_data['Attributes'])
        result_min_label.config(text=f"Minimum Score: {min_score}")
        result_max_label.config(text=f"Maximum Score: {max_score}")

    root = tk.Tk()
    root.title("Role Analyzer")

    # Load button
    load_button = ttk.Button(root, text="Load Player Data", command=load_file)
    load_button.pack(pady=10)

    # Dropdown for roles
    roles_data = get_all_role_data()
    role_var = tk.StringVar()
    role_dropdown = ttk.Combobox(root, textvariable=role_var, values=list(roles_data.keys()))
    role_dropdown.pack(pady=10)

    # Labels for results
    result_min_label = tk.Label(root, text="Minimum Score: N/A")
    result_min_label.pack()
    result_max_label = tk.Label(root, text="Maximum Score: N/A")
    result_max_label.pack()

    # Analyze button
    analyze_button = ttk.Button(root, text="Analyze Role", command=analyze_role)
    analyze_button.pack(pady=10)

    root.mainloop()

def get_all_role_data():
    return {
        #keepers
        'Goalkeeper': {
        'Role': 'Goalkeeper (Defend)',
            'Goalkeeping': {
                'Aerial Reach': 3, 'Command Of Area': 3, 'Communication': 3,
                'Eccentricity': 1, 'First Touch': 1, 'Handling': 3,
                'Kicking': 3, 'One On Ones': 3, 'Passing': 1,
                'Punching': 1, 'Reflexes': 5, 'Rushing Out': 3,
                'Throwing': 3
            },
            'Mental': {
                'Aggression': 3, 'Anticipation': 1, 'Bravery': 3,
                'Composure': 1, 'Concentration': 3, 'Decisions': 3,
                'Determination': 5, 'Flair': 1, 'Leadership': 1,
                'Off The Ball': 1, 'Positioning': 3, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 1
            },
            'Physical': {
                'Acceleration': 1, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 3, 'Pace': 1,
                'Stamina': 3, 'Strength': 5
            }
        },
        'Sweeper Keeper': {
        'Role': 'Sweeper Keeper (Defend)',
            'Goalkeeping': {
                'Aerial Reach': 3, 'Command Of Area': 3, 'Communication': 3,
                'Eccentricity': 1, 'First Touch': 1, 'Handling': 3,
                'Kicking': 3, 'One On Ones': 3, 'Passing': 1,
                'Punching': 1, 'Reflexes': 5, 'Rushing Out': 3,
                'Throwing': 3
            },
            'Mental': {
                'Aggression': 3, 'Anticipation': 1, 'Bravery': 3,
                'Composure': 1, 'Concentration': 3, 'Decisions': 3,
                'Determination': 5, 'Flair': 1, 'Leadership': 1,
                'Off The Ball': 1, 'Positioning': 3, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 1
            },
            'Physical': {
                'Acceleration': 1, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 3, 'Pace': 1,
                'Stamina': 3, 'Strength': 5
            }
        },
        # Defensive Roles
        'Ball Playing Defender (Defend)': {
            'Role': 'Ball Playing Defender (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 1, 'Dribbling': 1, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Full-Back (Defend)': {
            'Role': 'Full-Back (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Central Defender (Defend)': {
            'Role': 'Central Defender (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Complete Wing-Back (Support)': {
            'Role': 'Complete Wing-Back (Support)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Inverted Full-Back (Defend)': {
            'Role': 'Inverted Full-Back (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'No-Nonsense Centre-Back (Defend)': {
            'Role': 'No-Nonsense Centre-Back (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 1, 'Dribbling': 1, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'No-Nonsense Full-Back (Defend)': {
            'Role': 'No-Nonsense Full-Back (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 1, 'Dribbling': 1, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Inverted Wing-Back (Defend)': {
            'Role': 'Inverted Wing-Back (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Libero (Defend)': {
            'Role': 'Libero (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 1, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Wing-Back (Defend)': {
            'Role': 'Wing-Back (Defend)',
            'Technical': {
            'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
            'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
            'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
            'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
            'Technique': 3
            },
            'Mental': {
            'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
            'Composure': 3, 'Concentration': 3, 'Decisions': 3,
            'Determination': 3, 'Flair': 1, 'Leadership': 5,
            'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
            'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
            'Acceleration': 3, 'Agility': 3, 'Balance': 3,
            'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
            'Stamina': 5, 'Strength': 5
            }
        },
        'Advanced Playmaker (Support)': {
            'Role': 'Advanced Playmaker (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Wide Centre-Back (Defend)': {
            'Role': 'Wide Centre-Back (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Anchor (Defend)': {
            'Role': 'Anchor (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Box To Box Midfielder (Support)': {
            'Role': 'Box To Box Midfielder (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Attacking Midfielder (Support)': {
            'Role': 'Attacking Midfielder (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Ball Winning Midfielder (Defend)': {
            'Role': 'Ball Winning Midfielder (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Carrilero (Support)': {
            'Role': 'Carrilero (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Central Midfielder (Defend)': {
            'Role': 'Central Midfielder (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Defensive Midfielder (Defend)': {
            'Role': 'Defensive Midfielder (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Defensive Winger (Defend)': {
            'Role': 'Defensive Winger (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Deep Lying Playmaker (Defend)': {
            'Role': 'Deep Lying Playmaker (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Enganche (Support)': {
            'Role': 'Enganche (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Half Back (Defend)': {
            'Role': 'Half Back (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Inside Forward (Support)': {
            'Role': 'Inside Forward (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Inverted Winger (Support)': {
            'Role': 'Inverted Winger (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Mezzala (Support)': {
            'Role': 'Mezzala (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Raumdeuter (Attack)': {
            'Role': 'Raumdeuter (Attack)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Regista (Support)': {
            'Role': 'Regista (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 5, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 5
            },
            'Mental': {
                'Aggression': 3, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 5, 'Concentration': 3, 'Decisions': 5,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 5, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Roaming Playmaker (Support)': {
            'Role': 'Roaming Playmaker (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 5, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 5
            },
            'Mental': {
                'Aggression': 3, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 5, 'Concentration': 3, 'Decisions': 5,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 5, 'Work Rate': 5
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Shadow Striker (Attack)': {
            'Role': 'Shadow Striker (Attack)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Wide Playmaker (Support)': {
            'Role': 'Wide Playmaker (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Wide Midfielder (Defend)': {
            'Role': 'Wide Midfielder (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Segundo Volante (Support)': {
            'Role': 'Segundo Volante (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 5
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Winger (Support)': {
            'Role': 'Winger (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 1,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 5,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Complete Forward (Support)': {
            'Role': 'Complete Forward (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Advanced Forward (Attack)': {
            'Role': 'Advanced Forward (Attack)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Wide Target Forward (Support)': {
            'Role': 'Wide Target Forward (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 1, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 1, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 1, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'False Nine (Support)': {
            'Role': 'False Nine (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Poacher (Attack)': {
            'Role': 'Poacher (Attack)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 5, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Deep Lying Forward (Support)': {
            'Role': 'Deep Lying Forward (Support)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 3
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        },
        'Pressing Forward (Defend)': {
            'Role': 'Pressing Forward (Defend)',
            'Technical': {
                'Corners': 1, 'Crossing': 3, 'Dribbling': 3, 'Finishing': 3,
                'First Touch': 3, 'Free Kick Taking': 1, 'Heading': 5,
                'Long Shots': 3, 'Long Throws': 1, 'Marking': 5,
                'Passing': 3, 'Penalty Taking': 1, 'Tackling': 3,
                'Technique': 3
            },
            'Mental': {
                'Aggression': 5, 'Anticipation': 5, 'Bravery': 5,
                'Composure': 3, 'Concentration': 3, 'Decisions': 3,
                'Determination': 3, 'Flair': 3, 'Leadership': 5,
                'Off The Ball': 3, 'Positioning': 5, 'Teamwork': 5,
                'Vision': 3, 'Work Rate': 5
            },
            'Physical': {
                'Acceleration': 3, 'Agility': 3, 'Balance': 3,
                'Jumping Reach': 5, 'Natural Fitness': 5, 'Pace': 3,
                'Stamina': 5, 'Strength': 5
            }
        }
    }

# Start the GUI application
if __name__ == "__main__":
    create_interface()