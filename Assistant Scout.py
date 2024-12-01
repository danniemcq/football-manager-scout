import tkinter as tk
from tkinter import ttk
import json

def calculate_attribute_scores(player_data, role_data):
    score_min = 0
    score_max = 0
    
    # Function to parse attribute ranges
    def parse_range(value):
        if isinstance(value, str) and '-' in value:
            min_val, max_val = value.split('-')
            return int(min_val), int(max_val)
        elif isinstance(value, (int, float)):
            return value, value
        return 0, 0

    # Compare each attribute
    for category in ['Technical', 'Mental', 'Physical']:
        for attr, role_value in role_data[category].items():
            # Find matching player attribute
            player_value = player_data.get(attr, 0)
            
            # Get min and max values from role requirements
            min_req, max_req = parse_range(role_value)
            
            # Add to total scores
            score_min += min_req
            score_max += max_req

    return score_min, score_max

def create_interface():
    root = tk.Tk()
    root.title("Role Analyzer")

    # Create dropdown for roles
    roles = list(get_all_role_data().keys())
    role_var = tk.StringVar()
    role_dropdown = ttk.Combobox(root, textvariable=role_var, values=roles)
    role_dropdown.pack(pady=10)

    # Create result labels
    result_min_label = tk.Label(root, text="Minimum Score: ")
    result_min_label.pack()
    result_max_label = tk.Label(root, text="Maximum Score: ")
    result_max_label.pack()

    def analyze_role():
        selected_role = role_var.get()
        role_data = get_all_role_data()[selected_role]
        
        # Load player data from HTML file
        player_data = load_player_data('player_stats.html')  # You'll need to implement this
        
        min_score, max_score = calculate_attribute_scores(player_data, role_data)
        
        result_min_label.config(text=f"Minimum Score: {min_score}")
        result_max_label.config(text=f"Maximum Score: {max_score}")

    # Create analyze button
    analyze_button = ttk.Button(root, text="Analyze", command=analyze_role)
    analyze_button.pack(pady=10)

    root.mainloop()

def load_player_data(html_file):
    # This function would parse the HTML file and extract player attributes
    # You'll need to implement the HTML parsing logic here
    # Return a dictionary of player attributes
    pass

def get_all_role_data():
    roles_data = {
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
    
    return roles_data