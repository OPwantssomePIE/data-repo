import random
facts=["Oceans cover about 71% of the Earth’s surface.", 
"The Pacific Ocean is the largest and deepest of all the oceans.",
"The Atlantic Ocean is saltier than the Pacific Ocean.",
"The Indian Ocean contains the warmest waters among the oceans.",
"The Arctic Ocean is the smallest and shallowest of the oceans.",
"The average depth of the ocean is around 12,080 feet (3,682 meters).",
"The Mariana Trench in the Pacific Ocean is the deepest known part of the world’s oceans, reaching a depth of about 36,070 feet (10,994 meters).",
"The ocean contains approximately 97% of the Earth’s water.",
"Only about 3% of the world’s water is freshwater.",
"Oceans are responsible for producing more than 70% of the world’s oxygen through phytoplankton photosynthesis.",
"The Great Barrier Reef in Australia is the largest coral reef system in the world.", 
"Coral reefs cover less than 1% of the ocean’s area but provide habitat for about 25% of marine species.", 
"The ocean is home to an estimated one million species of animals, most of which remain undiscovered.",
"The blue whale, the largest animal on Earth, can reach lengths of over 100 feet (30 meters).", 
"The horseshoe crab, often considered a living fossil, has existed for over 450 million years.", 
"The ocean’s salinity averages around 35 parts per thousand (ppt), or 3.5% salt.",
"The Dead Sea, located between Jordan and Israel, is so salty that people can easily float on its surface due to the high salinity.",
"The Red Sea is named for the occasional blooms of red-colored cyanobacteria.",
"Some species of jellyfish are virtually immortal, as they can revert to their juvenile form after reaching maturity.",
"Oceans contain an estimated 20 million tons of gold dissolved in seawater, though it’s not currently economically feasible to extract it.", 
"Ocean currents help distribute heat around the planet, influencing climate and weather patterns.",
"The Gulf Stream, a warm ocean current, significantly affects the climate of the eastern United States and western Europe.",
"The Sargasso Sea, in the North Atlantic Ocean, is known for its floating mats of Sargassum seaweed.", 
"The ocean’s color varies based on depth and the presence of microscopic marine organisms, giving it a blue, green, or brownish tint.",
"Some deep-sea creatures produce their own light through bioluminescence, which helps them attract prey or mates and avoid predators.",
"'The Mid-Atlantic Ridge is a massive underwater mountain range that runs down the center of the Atlantic Ocean.",
"Ocean tides are caused by the gravitational pull of the Moon and the Sun.", 
"The highest tides in the world occur in the Bay of Fundy in Canada, with tidal ranges exceeding 50 feet (15 meters).",
"Shipwrecks and lost treasures are scattered throughout the world’s oceans, drawing treasure hunters and archaeologists alike.",
"The Bermuda Triangle, also known as the Devil's Triangle, is an area in the western part of the North Atlantic Ocean famous for unexplained disappearances of ships and aircraft.",
"The Titanic, which sank in 1912, rests about 12,500 feet (3,800 meters) below the surface of the North Atlantic Ocean.",
"Ocean acidification, caused by the absorption of excess carbon dioxide, is threatening marine life, particularly coral reefs and shellfish.",
"The concept of “blue carbon” refers to the role of coastal ecosystems like mangroves, seagrasses, and salt marshes in sequestering carbon dioxide.",
"Over 3 billion people rely on the ocean for their primary source of protein.", 
"The world’s largest fish, the whale shark, is a filter feeder that can reach lengths of up to 60 feet (18 meters).",
"The ocean’s temperature varies from -2°C (28°F) in polar regions to over 30Â°C (86Â°F) in equatorial regions.", 
"Oceanographers study the physical, chemical, biological, and geological aspects of the ocean.",
"The continental shelf is the submerged part of a continent that extends into the ocean and is relatively shallow.",
"The deep sea, also known as the abyssal zone, starts at a depth of about 6,000 feet (1,800 meters).", 
"The concept of the “ocean conveyor belt” describes the global circulation of ocean waters, which plays a vital role in regulating climate.",
"The Bermuda Petrel, also known as the Cahow, is a critically endangered seabird that breeds only in Bermuda.",
"Ocean exploration has led to numerous scientific discoveries, including the identification of new species and the development of new technologies.",
"The ocean’s vast and diverse ecosystems continue to captivate scientists, conservationists, and adventurers, inspiring ongoing efforts to protect and understand this essential part of our planet.",
"'Ocean currents can transport objects and debris across vast distances, leading to the phenomenon of “driftwood islands” in some remote areas.", 
"The ocean floor contains valuable minerals like manganese nodules, which have attracted interest for potential mining.",
"Some marine creatures, like sea cucumbers and certain types of crabs, play a vital role in cleaning the ocean floor by consuming detritus and waste.",
"Some species of sea turtles have been known to migrate thousands of miles across the ocean.",
"The “green flash” is a rare optical phenomenon that can sometimes be observed as a green spot on the horizon just after sunset or just before sunrise.",
"The ocean has its own weather patterns, including water spouts and waterspouts, which are tornadoes that form over water.",
"The ocean’s immense pressure at extreme depths can crush submarines and other man-made structures.",
"Submersibles and remotely operated vehicles (ROVs) are used to explore the depths of the ocean and gather data.",
"The concept of “thalassophobia” refers to a fear of the ocean or large bodies of water.",
"The ocean is not uniform in temperature; it has distinct layers with varying temperatures called thermocline.",
"The “Dumbo octopus” is a deep-sea octopus with large ear-like fins that resemble the ears of the Disney character Dumbo.",
"The ocean’s waves are caused by the wind’s friction on the surface of the water.",
"The Earth’s rotation influences the direction of ocean currents in the Northern and Southern Hemispheres.",
"Oceanographers use specialized equipment like CTD rosettes to measure temperature, salinity, and depth at various depths in the ocean.",
"The Titanic, which sank in 1912, rests about 12,500 feet (3,800 meters) below the surface of the North Atlantic Ocean.",
"The ocean’s waves are caused by the wind’s friction on the surface of the water.",
"The Earth’s rotation influences the direction of ocean currents in the Northern and Southern Hemispheres.",
"Oceanographers use specialized equipment like CTD rosettes to measure temperature, salinity, and depth at various depths in the ocean.",
"The ocean contains over 20 million tons of gold dissolved in seawater, though it is not currently economically viable to extract it.",
"Some species of fish, like the coelacanth, were thought to be extinct but were rediscovered alive in the deep ocean.",
"Giant kelp, a type of brown algae, can grow up to two feet per day and forms underwater forests in coastal regions.",
"The ocean’s acidity has increased by about 30 percentage since the Industrial Revolution due to the absorption of excess carbon dioxide.",
"Some marine animals, like sea cucumbers, are capable of regenerating lost body parts.",
"The deepest recorded free dive without scuba gear is over 800 feet (244 meters).",
"The “bioluminescent bay” in Vieques, Puerto Rico, is known for its waters that glow in the dark due to bioluminescent dinoflagellates.",
"Ocean acidification is particularly harmful to creatures with calcium carbonate shells or skeletons, like corals and mollusks.",
"Some fish, like clownfish, can change their sex in response to social cues or environmental factors.",
"The “Kraken” is a legendary sea monster from Scandinavian folklore often depicted as a colossal octopus or squid.",
"Some types of crabs can produce sounds by rubbing their claws or stridulating their legs together.",
"The oldest known oceanic crust is around 280 million years old, while continental crust can be much older.",
"Oysters can filter large amounts of water, helping to improve water quality in estuaries.",
"Some deep-sea creatures have evolved to withstand extreme cold, darkness, and pressure, making them well-suited to life in the abyssal zone.",
"The “Oceanic Desert” refers to regions of the ocean with low biological productivity due to nutrient scarcity.",
"The “Twilight Zone” of the ocean, known as the mesopelagic zone, is where sunlight begins to fade, and bioluminescent organisms become more common.",
"Marine snow consists of tiny particles, dead organisms, and organic matter that drift down from the surface to the ocean floor.",
"The ocean contains various “dead zones” with low oxygen levels, often caused by excessive nutrient runoff from agriculture.",
"Seashells are made primarily of calcium carbonate and are the protective outer layer of mollusks like clams and snails.",
"The Pacific Ocean is so vast that it covers more area than all the Earth’s landmasses combined.", 
"The Amazon River carries more freshwater into the Atlantic Ocean than any other river in the world.",
"The ocean is not always salty; its salinity can vary due to factors like rainfall, evaporation, and freshwater input from rivers.",
"The “Black Smokers” are hydrothermal vents on the ocean floor that release hot, mineral-rich water, creating unique ecosystems.",
"Sea otters are known for using tools like rocks and shells to break open shellfish for food.",
"The “Deepwater Horizon” oil spill in the Gulf of Mexico in 2010 was one of the largest environmental disasters in history.",
"Some whales undertake the longest migrations of any animals, traveling thousands of miles between their feeding and breeding grounds.",
"The Great Barrier Reef is visible from space and is considered one of the seven natural wonders of the world.",
"The “Roaring Forties”, “Furious Fifties” and “Screaming Sixties” are nicknames for the strong westerly winds found in the Southern Ocean.",
"Oceanographers use satellite technology to monitor sea surface temperatures, ocean currents, and sea level rise.",
"The Caspian Sea is the world’s largest enclosed inland body of water, technically making it a lake rather than an ocean.",
"The “Bloop” is a mysterious and extremely loud sound recorded in the Pacific Ocean in 1997, the source of which remains unknown.",
"The ocean’s temperature influences the type and distribution of marine life, with warm-water and cold-water species residing in different regions.",
"Tsunamis, often caused by underwater earthquakes or volcanic eruptions, can travel across the ocean at speeds of up to 500 miles per hour (800 kilometers per hour).",
"The ocean contains a vast array of shipwrecks and sunken aircraft, making it a treasure trove for underwater archaeologists.",
"Ocean exploration has led to technological advancements, including the development of deep-sea submersibles and remotely operated vehicles (ROVs).",
"The ocean plays a vital role in shaping global weather patterns, influencing everything from monsoons to El Niño events.",
"The “Blue Planet” series by Sir David Attenborough has provided captivating insights into the mysteries of the ocean and its inhabitants.",
"The ocean continues to be a source of inspiration, exploration, and scientific discovery, reminding us of its profound importance to life on Earth."]
def search_data():
    print(facts[random.randint(0,99)])

search_data()