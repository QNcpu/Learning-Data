for beast in range(1,76):
    for bird in range(1,76):
        if beast*6+bird*4==76 and beast*4+bird*2==46:
            print(f"beast:{beast},bird:{bird}")