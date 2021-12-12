# coding: utf-8
    # Python Scripts for the Netrunner CCG definition for OCTGN
    # Copyright (C) 2012  Konstantine Thoukydides

    # This python script is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this script.  If not, see <http://www.gnu.org/licenses/>.

    
import re

#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------

mdict = dict( # A dictionary which holds all the hard coded markers (in the markers file)
             Advance =                 ("Advance", "73b8d1f2-cd54-41a9-b689-3726b7b86f4f"),
             Generic =                 ("Generic", "b384957d-22c5-4e7d-a508-3990c82f4df6"),
             Bits =                    ("Bits", "19be5742-d233-4ea1-a88a-702cfec930b1"),
             Scored =                  ("Scored", "10254d1f-6335-4b90-b124-b01ec131dd07"),
             Not_rezzed =              ("Not rezzed", "8105e4c7-cb54-4421-9ae2-4e276bedee90"),
             Derezzed =                ("Derezzed", "ae34ee21-5309-46b3-98de-9d428f59e243"),
             Trace_value =             ("Trace value", "01feb523-ac36-4dcd-970a-515aa8d73e37"),
             Link_value =              ("Link value", "3c429e4c-3c7a-49fb-96cc-7f84a63cc672"),
             PlusOnePerm =             ("Permanent +1", "f6230db2-d222-445f-85dd-406ea12d92f6"),
             PlusOne=                  ("Temporary +1", "aa261722-e12a-41d4-a475-3cc1043166a7"),
             MinusOne=                 ("Temporary -1", "48ceb18b-5521-4d3f-b5fb-c8212e8bcbae"),
             DaemonMU =                ("Daemon MU", "6e46d937-786c-4618-b02c-d7d5ffd3b1a5"),
             BaseLink =                ("Base Link", "226b0f44-bbdc-4960-86cd-21f404265562"),
             virusButcherBoy =         ("Butcher Boy virus","5831fb18-7cdf-44d2-8685-bdd392bb9f1c"),
             virusCascade =            ("Cascade virus","723a0cca-7a05-46a8-a681-6e06666042ee"),
             virusCockroach =          ("Cockroach virus","cda4cfcb-6f2d-4a7f-acaf-d796b8d1edee"),
             virusGremlin =            ("Gremlin virus","032d2efa-e722-4218-ba2b-699dc80f0b94"),
             virusThought =            ("Thought virus","811b9153-93cb-4898-ad9f-68864452b9f4"),
             virusFait =               ("Fait virus","72c89567-72aa-446d-a9ea-e158c22c113a"),
             virusBoardwalk =          ("Boardwalk virus","8c48db01-4f12-4653-a31a-3d22e9f5b6e9"),
             virusIncubate =           ("Incubate virus","eccc2ee3-2bca-4563-8196-54de4909d313"),
             virusPattel =             ("Pattel virus","93a124c4-d2fe-4f58-9531-1396675c64dd"),
             protectionMeatDMG =       ("Meat Damage protection","f50fbac7-a147-4941-8d77-56cf9ea672ea"),
             protectionNetDMG =        ("Net Damage protection","84527bb1-6b34-4ace-9b11-7e19a6e353c7"),
             protectionBrainDMG =      ("Brain damage protection","8a0612d7-202b-44ec-acdc-84ff93e7968d"),
             protectionNetBrainDMG =   ("Net & Brain Damage protection","42072423-2599-4e70-80b6-56127b7177d9"),
             protectionAllDMG =        ("Complete Damage protection","04d72620-17d1-4189-9abb-a2c48ddf7d42"),
             protectionVirus =         ("Virus protection","6242317f-b706-4e39-b60a-32958d00a8f8"),
             BrainDMG =                ("Brain Damage","05250943-0c9f-4486-bb96-481c025ce0e0"))

             
regexHooks = dict( # A dictionary which holds the regex that then trigger each core command. 
                   # This is so that I can modify these "hooks" only in one place as I add core commands and modulators.
                  GainX =              re.compile(r'\b(Gain|Lose|SetTo)([0-9]+)'),
                  CreateDummy =        re.compile(r'\bCreateDummy'),
                  ReshuffleX =         re.compile(r'\bReshuffle([A-Za-z& ]+)'),
                  RollX =              re.compile(r'\bRoll([0-9]+)'),
                  RequestInt =         re.compile(r'\bRequestInt'),
                  DiscardX =           re.compile(r'\bDiscard[0-9]+'),
                  TokensX =            re.compile(r'\b(Put|Remove|Refill|Use|Infect)([0-9]+)'),
                  TransferX =          re.compile(r'\bTransfer([0-9]+)'),
                  DrawX =              re.compile(r'\bDraw([0-9]+)'),
                  ShuffleX =           re.compile(r'\bShuffle([A-Za-z& ]+)'),
                  RunX =               re.compile(r'\bRun([A-Za-z& ]+)'),
                  TraceX =             re.compile(r'\bTrace([0-9]+)'),
                  InflictX =           re.compile(r'\bInflict([0-9]+)'),
                  ModifyStatus =       re.compile(r'(Rez|Derez|Expose|Trash|Uninstall|Possess|Exile)'),
                  SimplyAnnounce =     re.compile(r'\bSimplyAnnounce'),
                  ChooseKeyword =      re.compile(r'\bChooseKeyword'),
                  CustomScript =       re.compile(r'\bCustomScript'),
                  UseCustomAbility =   re.compile(r'\bUseCustomAbility'))

automatedMarkers = [ #Used in the Inspect() command to let the player know if the card has automations based on the markers it puts out.
         'Rent-to-Own Contract',
         'Data Raven'
         'Fang'
         'Fang 2.0'
         'Fragmentation Storm'
         'Rex'
         'Cerberus'
         'Doppelganger Antibody'
         'Armageddon'
         'Baskerville'
         'The Shell Traders'
         'Butcher Boy',
         'Boardwalk',
         'Incubator',
         'Viral Pipeline',
         'Taxman',
         'Skivviss',
         'Scaldan']

markerRemovals = { # A dictionary which holds the costs to remove various special markers.
                       # The costs are in a tuple. First is actions cost and then is bit cost.
                     'Fang' :                        (1,2),
                     'Data Raven' :                  (1,1),
                     'Fragmentation Storm' :         (1,1),
                     'Rex' :                         (1,2),
                     'Crying' :                      (1,2),
                     'Cerberus' :                    (1,4),
                     'Baskerville' :                 (1,3),
                     'Doppelganger' :                (1,4),
                     'Mastiff' :                     (1,4)}
turns = [
   'Start of Game',
   "It is now Corporation's Turn",
   "It is now Runner's Turn",
   "It is now End of Turn"]

trashEasterEgg = [
   "You really shouldn't try to trash this kind of card.",
   "No really, stop trying to trash this card. You need it.",
   "Just how silly are you?",
   "You just won't rest until you've trashed a setup card will you?",
   "I'm warning you...",
   "OK, NOW I'm really warning you...",
   "Shit's just got real!",
   "Careful what you wish for..."]
trashEasterEggIDX = 0
 
ScoredColor = "#00ff44"
SelectColor = "#009900"
EmergencyColor = "#ff0000"
DummyColor = "#000000" # Marks cards which are supposed to be out of play, so that players can tell them apart.
RevealedColor = "#ffffff"
PriorityColor = "#ffd700"
InactiveColor = "#888888" # Cards which are in play but not active yer (e.g. see the shell traders)

Xaxis = 'x'
Yaxis = 'y'
