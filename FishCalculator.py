Length = int(input("Please input the length: "))
Girth = int(input("Please input the girth: "))

# Calculator for the fish weight 
def fish_weight(Length, Girth):
    FishWeight = Girth * Girth * Length / 800
    return FishWeight
FishWeight = fish_weight(Length, Girth)
print(f'The fish weight is {FishWeight:.2f} pounds')

#Data of fish sizes to determine the input given by user
def fish_sizes():
    fish_sizes_list = ["Small fish", "Medium fish", "Big fish", "Giant Fish"]
    return fish_sizes_list
fish_sizes_list = fish_sizes()
print(fish_sizes_list)

#Fish Classification
def classify_fish(FishWeight):
    if FishWeight < 41:
        classification = "Small fish"
    elif FishWeight < 99:
        classification = "Medium fish"
    elif FishWeight < 174:
        classification = "Big fish"
    else:
        classification = "Giant fish"
    return f"The fish is classified as {classification}"

print(classify_fish(FishWeight))