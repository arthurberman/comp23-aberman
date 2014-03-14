"The Salesman" by Arthur Berman

Selling to is an action applying to one visible thing.
Understand "sell the sword to [the person]" as selling to. Understand "sell sword to [the person]" as selling to.
Understand "drink [something]" as drinking. 
Understand "talk to [the person]" as talking to. Understand "talk to [something]" as talking to. Talking to is an action applying to one visible thing. 

Instead of selling to Gerome Slowarm:
	if a sword is not carried by the player, say "You don't have the sword." instead;
	if a sword is carried by the player:
		Move the sword to Gerome Slowarm;
		say "Gerome thanks you for the fine sword, and gladly parts with 150 points.";
		increase the score by 150;
		rule succeeds;

Instead of selling to Matthias Greyhammer:
	if a sword is carried by the player:
		Move the sword to Matthias Greyhammer;
		Say "Matthias thanks you for the fine sword, at such a reasonable price. He gives you 100 points in exchange.";
		increase the score by 100;
		rule succeeds. 



When play begins:
say "It has been 1000 years since the Last Sundering, when the evil that sleeps on the edge of the world was banished again, as it has been for millenia. But now, the Ancient Fog has risen, and in the mist demons have awoken. As beasts of legend once again take shape and weave their devastation across the land, heroes from around the world have taken up arms in the defense of their home. And of course, somebody has to sell them their weapons..."

The player is in the store. 

Matthias Greyhammer is a man. Matthias Greyhammer is in the store. The description is "A stout man in leather armor. He is clearly a capable fighter."

Gerome Slowarm is a man. Gerome Slowarm is in the store. The description is "A fat man who walks with a severe limp. He cannot possibly be a capable fighter, but here he is, looking for gear."

The priest is a man. The priest is in the church. The description is "A tall, gaunt fellow dressed in elaborate finery, the priest looks out of place amongst the squalor and disarray that has overcome the town."

The cat is an animal. The cat is in the town square.  The description is "This mangy cat has seen better days, but it still seems spry."

Instead of talking to Matthias Greyhammer:
	say "The man turns to you and says 'Hello, you fine fellow. I'm looking to buy a sword. I would be willing to pay 100 points for it.'"
Instead of talking to Gerome Slowarm:
	say "Gerome says 'Hello. I would be willing to pay 150 points for that sword if you'd part with it.'"
Instead of talking to Muriel:
	say "Muriel says, 'Bug off, you twit. I don't want any of what you're selling. Won't do no good neither. Keh-heh-heh-heh.'"
Instead of talking to the priest:
	say "The priest says 'Now is the time to make a donation, for the time of judgment is nigh. Perhaps something golden, if you have it.'"
Instead of taking the cat:
	say "The cat scurries away.";
	remove the cat from play.
Instead of taking the wriggling bag:	
	say "Muriel yelps as you snatch at the bag, before starting a guttural chant. You feel bile rising as you realise that you are being cursed. You crumple to the ground and writhe in agony before dying.";
	End the story.

The wriggling bag is a thing. 



Muriel is a woman. Muriel is in the town square. Muriel carries a wriggling bag. The description is "A wizened old crone wearing a ragged cloak. An oily, slick lock of hair droops across her forehead, but her head is otherwise bald. A bag slung across her shoulder wriggles slightly."

A sword is a thing.  The description is "The only worthwhile piece of equipment you have to sell. You should try to find somebody who will buy it. Try to 'sell the sword to' somebody."

The Store is a room. A sword is here. "You stand behind the counter of your Adventuring Supply Store. Various customers mill about as they examine your various goods. Your sword leans against the wall, but you're a merchant and don't have the strength or skill needed to fight with such a weapon. " 

The Front Door is a door. It is north of the Store. It is south of the Town Square. It is open. 

The main gate is a door. It is north of the North Wall. It is closed and locked. The main gate has a matching key the Gate Key. 

The gate key is in the town hall. 

The tankard of ale is a thing. The description is "This tankard almost certainly does not contain ale anymore. The corruption that surrounds everything appears to have reduced this to a purple mass."

The bar cellar is a room. It is down from the tavern. The description is "This nondescript cellar has a single shaft of light from a small window. Clearly the whole place has been cleared out."

The tower is a room. It is west of the top of the wall. The description is "This tower is a vantage point from which the whole world seems to stretch out before you. However, due to the mist, there really isn't much to see. "

Instead of drinking the tankard of ale:
	say "You retch violently before falling to the floor, dead.";
	End the story. 

The tavern is a room. The tavern is north of the east wall. The tankard of ale is here. The description of the tavern is "This seedy bar used to be the most bustling place in town. Now, the bar is empty. Not even the bartender is here, having fled east. A tankard of ale sits on the counter."

The Town Square is a room. It is south of the North Wall. It is west of the East Wall. "The once-bustling town square is eerily quiet. The black mist that lingers across the world is thin here, but still present. Apart from the city guards, the only other person in the square is an old woman, who you recognize as Muriel, the Witch. The city walls loom overhead to the north and east. The church is to the west, with its enormous gates open to anybody willing to donate."

The North Wall is a room. Up from the North Wall is The Top of the Wall. The description is "This immense wall may be the only thing protecting the town from certain destruction. An enormous gate stands barred and locked. If any of the demons were to attack, surely this wall would stop them...
You can go up the wall."
The Top of the Wall is a room. The description is "You can see an enormous bank of fog."
The East Wall is a room. The description is "this immense wall to the east is impassable. You hope it will be enough to defend the town in the event of an attack."

The town hall is a room. The town hall is west of the north wall. The description is "Once the center of government in the city, the town hall is now deserted."

The church is a room. The church is west of the church door. The description is "The church has never been this empty. A chorus of prayers drifts ethereally through the building, but nobody is here save for the priest."

The church door is a door. It is west of the town square. It is open. 

The enormous bank of fog is in the top of the wall. It is scenery. The description is "This obscuring cloud almost seems to growl menacingly. Looking at it hurts the eyes, not because it is bright but because it seems to sap light from the space in front of you. "

The Attack is a scene. The Attack begins when the turn count is 10. The Attack ends tragically when the time since The Attack began is 5 minutes. 

Every turn during The Attack:
	repeat through Table of Attack Events:
		say "[event entry][paragraph break]";
		blank out the whole row;
		rule succeeds;
	If Matthias Greyhammer carries a sword:
		say "Matthias Greyhammer takes his newly acquired sword and slays the horrifying beast that threatens the town. You are safe and able to sell your wares for another day, but how much longer will this uneasy safety last?";
		End the game in victory.

When the attack begins:
	If Gerome Slowarm carries a sword:
		Gerome attacks in three turns from now;
	If Matthias Greyhammer carries a sword:
		Matthias attacks in three turns from now. 
		
At the time when Matthias attacks:
	say "Matthias Greyhammer takes his newly acquired sword and slays the horrifying beast that threatens the town. You are safe and able to sell your wares for another day, but how much longer will this uneasy safety last?";
	End the game in victory.

At the time when Gerome attacks:
	If Gerome Slowarm carries a sword:
		say "Gerome Slowarm takes his new sword and charges the horrifying beast, and is summarily squelched by three tons of demon-claw.".
		
Instead of opening the main gate:
	say "By opening the gate, you have allowed the monsters entrance to the city. Demons and monsters wreak havoc and destroy everything in their reach, starting with you.";
	End the story.
When the Attack ends tragically:
	say "Alas, the horrifying demonic beast has overwhelmed the city, and in so doing has ended your life. If only you had been a better businessman and sold some goods to somebody who could actually defend the city.";
	End the story.
		
Table of Attack Events
event
	"A horrifying roar fills the air."
	"Screams and cries ring out."
	"A monstrous shadow covers the [location]."
	"A beast with one-thousand eyes peers down from the sky above. Clearly the enormous walls were inadequate to keep this monster out."
	"The Beast inhales, and a horrible miasma oozes from his throat. He is about to drown the city in death. "