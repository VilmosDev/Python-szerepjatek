SCENES = {

    # BOLT
    "start": {
        "text": "Kani éhes. Nincs pénze kolbászra.",
        "choices": [
            ("Megpróbál lopni a boltban", "caught"),
            ("Nem lop, de éhes marad", "caught")
        ]
    },

    "caught": {
        "text": "A rendőrök elkapják Kani-t.\nBörtönbe kerül.",
        "choices": [
            ("Tovább", "cell")
        ]
    },

    # CELLA
    "cell": {
        "text": "Kani a rozsdás cellában ül.",
        "choices": [
            ("Képzeletben monitort lát és ütni kezdi a rácsokat", "hallway"),
            ("Feladja", "bad_end")
        ]
    },

    # FOLYOSO
    "hallway": {
        "text": "A folyosón két irány van.",
        "choices": [
            ("Balra megy", "yard"),
            ("Jobbra megy", "guard")
        ]
    },

    "guard": {
        "text": "Egy őr áll előtted.",
        "choices": [
            ("Eltereli egy kővel", "yard"),
            ("Lebukik", "cell")
        ]
    },

    # DOMINIK
    "yard": {
        "text": "Az udvaron találkozol Dominikkal.",
        "choices": [
            ("Beszél vele", "dominik"),
            ("Tovább mész egyedül", "escape_alone")
        ]
    },

    "dominik": {
        "text": "Dominik felajánlja a segítségét.",
        "choices": [
            ("Elfogadod", "escape_together"),
            ("Elutasítod", "escape_alone")
        ]
    },

    # ACT 5 – ESCAPE
    "escape_together": {
        "text": "Kani és Dominik együtt próbálnak megszökni.",
        "choices": [
            ("Tovább", "good_end")
        ]
    },

    "escape_alone": {
        "text": "Kani egyedül próbál megszökni.",
        "choices": [
            ("Tovább", "neutral_end")
        ]
    },

    # STORY VEGE
    "good_end": {
        "text": "Sikerül megszökniük.\nJÓ BEFEJEZÉS",
        "choices": []
    },

    "neutral_end": {
        "text": "Kani megszökik, de Dominik marad.\nKESERÉDES VÉG",
        "choices": []
    },

    "bad_end": {
        "text": "Kani sosem jut ki a cellából.\nROSSZ VÉG",
        "choices": []
    }
}
