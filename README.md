# fiasco-relationship-generator
A relationship generator for the fiasco rpg

See it in action [here](http://monknomo.github.io/fiasco-relationship-generator/)

This is a website that takes the elements from a [Fiasco ](http://www.bullypulpitgames.com/games/fiasco/) scenario and randomly creates relationships between players

[See it in action](https://monknomo.neocities.org/fiasco-relationship-generator/index.html)

Scenario contributions welcome!

Scenarios should be a json format file called "playset.json"

    {  
        "metadata":{  
            "playsetUrl":"the url of the playset",
            "fiascoUrl":"http://www.bullypulpitgames.com/games/fiasco/",
            "creator":"Jason Morningstar",
            "movies":[  "inspiration goes here"  ],
            "boilerplate":"This playset is an accessory for the Fiasco role-playing game by Bully Pulpit Games.  This playset is copyright 2010 by Jason Morningstar. Fiasco is copyright 2009 by Jason Morningstar. All rights are reserved.  For more information about Fiasco or to download other playsets and materials, visit www.bullypulpitgames.com.  If you'd like to create your own playset or other Fiasco-related content, we'd like to help. Write us at info@bullypulpitgames.com.",
            "score":"Description goes here",
            "playsetName":"playset name goes here"
        },
        "needs":{  
            "need category name goes here, 6 total":[  
                "specific need name goes here, 6 to a list"
            ],
            "broadCategories":[  
                "list the 6 category names here"
            ]
        },
        "relationships":{  
            "relationship category name goes here, 6 total":[  
                "specific relationship name goes here, 6 to a list"
            ],
            "broadCategories":[  
                "list the 6 category names here"
            ]
        },
        "totemicObjects":{ 
            "totemic object category name goes here, 6 total":[  
                "specific totemic object name goes here, 6 to a list"
            ],
            "broadCategories":[  
                "list the 6 category names here"
            ]    
        },
        "locations":{  
            "location category name goes here, 6 total":[  
                "specific location name goes here, 6 to a list"
            ],
            "broadCategories":[  
                "list the 6 category names here"
            ] 
        }
    }


