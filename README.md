﻿Netrunner CCG plugin for OCTGN 3.4
===================================


Netrunner s an asymmetrical cyberpunk Card Game for two players.&#xD;&#xD;Set in the dystopian future of Cyberpunk 2020, the game pits an anonymous megacorporation and its massive resources against the subversive talents of lone runners.


**(This is the original Netrunner game from 1996!)**


This is a repository for the a game definition for the [Online Card and Tabletop Gaming Network (OCTGN)](https://www.octgn.net/).

* Automation Rank: **A** *(This game definition contains significant cards automations to allow the game to play faster with less mistakes.)*

Available Sets
---------

Currently Netrunner does not utilize OCTGN auto-generated proxies to play. You'll need to download the card image packs to be able to play. 

The link below will provide you with a download bundle you can import into OCTGN by the "Add Image Packs" function in the game manager

* [Netrunner Card Images Bundle](http://dbzer0.com/pub/Netrunner/Sets/Netrunner-Sets-Bundle.o8c) *(Last Updated 14/04/2013)*


Gameplay
--------

Some basic instructions on how to use the new system will be forthcoming, but things should be fairly intuitive anyway. Some basic things to remember

* First thing you do after you load a deck is Setup (Ctrl+Shift+S)
* At the start of your turn, declare it with F1
* At the end of your turn, declare it with F12. Make sure the game announces that your turn has ended and is not expecting you to discard down to your max hand size ;)
* Play/Install cards from your hand by double-clicking them. Use cards on the table in the same way. 
* Always try to Trash or Uninstall cards by using the relevant function in the menu (e.g. 'del' key)
  * If you want to trash the card of an opponent, _first let them know_ then target the card (shift+click) and use the "Trash Target" options in the **table menu** (i.e. right-click on an empty spot on the table)
* Only ever drag & drop cards from your hand to the table, or from the table/hand to your trash, if there's no other way.

And some more advanced stuff:

* If you're the corp, remove all viruses by double-clicking your "Virus Scan" card. If you're the runner, remove Sentry markers by double-clicking on your "Technical Difficulties" card.
* Most card will automatically trigger their abilities when played/scored/rezzed so you don't need to do anything else. Pay attention to the notification area for messages from them.
* Cards with abilities which increase your MU, Hand Size, etc will automatically increase it when they come into play and reduce it when they go away, as long as you don't drag&drop them in or out of the table manually. Use the built-in commands for that. Rez, Derez, Trash etc
* Cards with abilities you activate while they're in play (like programs, agendas, upgrades etc) will trigger them when you double-click on them. If they have more than one ability (such as most icebreakers), the game will prompt you to select one and pay the appropriate cost.
* Cards which reduce the cost of other card's abilities, will also automatically work. If you have a card which has tokens which can pay the cost for activating icebreakers, they will be automatically used when you use one such ability. If you have more than one of these cards which can affect such costs they will be triggered in the order you put them on the table. If you wanted to use the tokens from another card instead, you can simply drag the token manually to the other card afterwards.
* There are cards which will automatically do damage to your opponent and thus discard random cards from their hand. Due to the way OCTGN works, this may crash the game if you opponent was manipulating the same card. There is a warning before all such damage that will warn you to inform your opponent to be hands-off while the effect is in progress. This warning will also give your opponent the opportunity to play cards which prevent damage.
* Yes, cards which reduce damage taken have been automated and work automatically depending on the kind of damage you take. As before, they too get triggered by the order they've been put on the table, so if you didn't want to lose the counters from one particular card, just drag them in from the card you did want to use.
* Some cards require that you select a target from the table or your hand. Do this before you play or activate the card. If you don't the action will abort and the game will inform you to select your targets first.  As always, keep your eye on the chatbox for such warnings.
* Cards which have effects which trigger at start/end of turn (i.e. refilling bit markers on them) will automatically work.
* Cards which put markers on a player, which __themselves__ have an automated ability (i.e. Fang, Baskerville, Armageddon etc) will _also_ automatically work.
* If you don't like some or all the automations, you can disable some or all of them. Go to the game menu, and you can disable damage automations (i.e. your opponent will have to use the damage options manually), Damage Prevention, Turn Start/End automations and Play/Score/Rez Automations (i.e. mostly everything). If you find that you'd rather do everything manually, just disable all of them and you'll have an experience as with most generic card game engines.
* Cards with multiple effects will request you to select one of them when you activate them. Select an ability by putting their number in the window that pop's up. You should be able to get the idea of which ability is each from the parsed script.

Phew, that should be the most basic things about the new automations. If you're not sure if a card is automated, simply use the 'Inspect' function and the game will inform you of the details.

Honorary mentions of complex cards that I've managed to automate:
* Arasaka Owns You
* Mystery Box
* Playful AI
* The Shell Traders
* Emergency Self Construct

and many many more

Enjoy!

Screenshots
---------
(Click for larger size)

An Epic Run is starting.

[![](http://i.imgur.com/gTiVfl.jpg)](http://fav.me/d5c7r4j)

How the custom fonts look like

[![](http://i.imgur.com/1Zcjy.png)](http://i.imgur.com/1Zcjy.png)
