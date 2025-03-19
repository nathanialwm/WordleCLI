from flask import Flask, jsonify

app = Flask(__name__)

# 60 easy five-letter words
easy_words = [
    "apple", "table", "chair", "happy", "smile", "light", "water", "bread", "piano", "candy",
    "house", "fruit", "dance", "magic", "color", "sugar", "juice", "party", "earth", "river",
    "clock", "watch", "plant", "stone", "money", "sound", "frame", "track", "field", "beach",
    "storm", "clear", "round", "space", "peace", "brave", "glass", "floor", "novel", "comic",
    "clown", "heart", "medal", "noble", "value", "drink", "laugh", "cloud", "blade", "truth",
    "dream", "guest", "pride", "smoke", "fresh", "grain", "spice", "toast", "extra", "charm"
]

# 60 medium five-letter words
medium_words = [
    "brisk", "crisp", "droll", "flame", "glory", "spice", "shiny", "bloom", "frost", "thick",
    "twirl", "gleam", "blaze", "drift", "snarl", "surge", "plume", "evoke", "sprig", "glint",
    "shrew", "slyly", "scamp", "vexed", "smoky", "brawn", "clout", "feint", "glade", "hasty",
    "perky", "vivid", "snide", "trite", "quiet", "quick", "rapid", "snuff", "waver", "wacky",
    "merry", "zesty", "nifty", "rogue", "pivot", "eject", "spurt", "gloom", "slant", "glare",
    "whiff", "plump", "frond", "swell", "flush", "crypt", "caper", "mirth", "gloss", "rhyme"
]

# 60 hard five-letter words (a mix of obscure or less common words)
hard_words = [
    "fjord", "glyph", "nymph", "buxom", "pique", "vexed", "wryly", "jazzy", "knurl", "quips",
    "xylyl", "stymy", "zowie", "tryst", "psalm", "waltz", "axiom", "kedge", "blitz", "phlox",
    "mauve", "cwtch", "gloze", "squib", "sloyd", "thole", "quoin", "sprit", "swash", "bream",
    "flump", "snarf", "scurf", "whelm", "lurid", "chirk", "gypsy", "crimp", "prink", "knave",
    "glitz", "mimsy", "gunky", "pukka", "froth", "chump", "wince", "zippy", "jowar", "pudgy",
    "sward", "knout", "lithe", "dimly", "scion", "blurb", "flair", "wield", "fugue", "spurn"
]

@app.route('/easy')
def get_easy():
    return jsonify(easy_words)

@app.route('/medium')
def get_medium():
    return jsonify(medium_words)

@app.route('/hard')
def get_hard():
    return jsonify(hard_words)

if __name__ == '__main__':
    app.run(debug=True)
