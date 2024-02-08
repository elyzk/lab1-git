/**
 * Takes a string and returns each word that appears exactly twice (case insensitive)
 * Args: the string to analyze
 * Returns: prints each word that is doubled, in the same case as the first occurrence of that word
 */


// Process string
let args = process.argv.slice(2)

if (args.length == 0) {
    console.log("ERROR: You must provide at least one string")
    process.exit()
} 

let string = args.join(" ")
let word_freq = new Map()

// Count occurrences of each word
for (let word of string.split(" ")) {
    if (word_freq.has(word.toLowerCase())) {
        word_freq.get(word.toLowerCase())[1] += 1
    } else {
        word_freq.set(word.toLowerCase(), [word, 1])
    }
}

// Print all doubled words
for (let word of word_freq.keys()) {
    if (word_freq.get(word)[1] == 2) {
        console.log(word_freq.get(word)[0])
    }
}
