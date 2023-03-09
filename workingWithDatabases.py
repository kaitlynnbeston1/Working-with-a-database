Marvel_Superheros = {
  "Spiderman" : {
           "Name" : "Peter Parker",
           "Weapons" : ["Webbing"],
           "Super Powers" : ["Speed", "Reflexes",
                             "Spider-Sense"],
           "Weaknesses" : ["Ethyl Chloride Pesticide"], },
  "Thing" : {
           "Name": "Ben Grimm",
           "Weapons": ["Fists"],
           "Super Powers": ["Immortal", "Super Strength",
                      "Enhanced Lung Capacity", "Good Fighter"],
         "Weaknesses": ["None"], },  
  "Baby_Groot" : {
           "Name" : "Baby Groot",
           "Weapons" : ["Strong Branches"],
           "Super Powers" : ["Self-Healing", "Controls Plant",
                            "Immune to Fire"],
           "Weaknesses" : ["Termites"], },
  "Ironman" : {
           "Name" : "Tony Stark",
           "Weapons" : ["Ironman Suit", "AI", "Blasters"],
           "Super Powers" : ["Smart", "Rich"],
           "Weaknesses" : ["Arrogant"], },
  "Deadpool" : {
           "Name" : "Wade Wilson",
           "Weapons" : ["Katanas", "Grenades", "Guns"],
           "Super Powers" : ["Speed", "Bullet Proof",
                             "Self-Healing"],
           "Weaknesses" : ["Women", "Ugly"], },
  "Antman" : {
           "Name" : "Scott Lang",
           "Weapons" : ["Antman Suit"],
           "Super Powers" : ["Communication with Insects",
                             "Sound Amplification"],
           "Weaknesses" : ["Lacks Ability Control"], },
}
for k in Marvel_Superheros.keys():
    print(k)

for k in Marvel_Superheros:
    for n in Marvel_Superheros[k]:
        if n == "Name":
           print(Marvel_Superheros[k][n])

           
for hero, info in Marvel_Superheros.items():
    print(hero)
    name = info["Name"]
    weapons = info["Weapons"]
    powers = info["Super Powers"]
    weaknesses = info["Weaknesses"]
    print("{:<20} {:<20}".format("Name:", name))
    print("{:<20}".format("Weapons:"))
    for weapon in weapons:
        print("{:<20}".format(weapon))
    print("{:<20}".format("Super Powers:"))
    for power in powers:
        print("{:<20}".format(power))
    print("{:<20}".format("Weaknesses:"))
    for weakness in weaknesses:
        print("{:<20}".format(weakness))