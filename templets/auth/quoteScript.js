const nextBtn = document.getElementById('nextQuote');
let quote = document.getElementById('quote');
let author = document.getElementById('author');

const quotes = [
    {
        quote: 'You can get everything in life you want if you will just help enough other people get what they want',
        author: 'Zig Ziglar'
    },
    {
        quote: 'Inspiration does exist, but it must find you working.',
        author: 'Pablo Picasso'
    },
    {
        quote: 'Don\'t settle for average. Bring your best to the moment. Then, whether it fails or succeeds, at least you know you gave all you had.',
        author: 'Angela Bassett'
    },
    {
        quote: 'Show up, show up, show up, and after a while the muse shows up, too.',
        author: 'Isabel Allende'
    },
    {
        quote: 'Don\'t bunt. Aim out of the ballpark. Aim for the company of immortals',
        author: 'David Ogilvy'
    },
    {
        quote: 'I have stood on a mountain of no’s for one yes.',
        author: 'Barbara Elaine Smith'
    },
    {
        quote: 'If you believe something needs to exist, if it\'s something you want to use yourself, don\'t let anyone ever stop you from doing it',
        author: 'Tobias Lütke'
    }
];

let quoteLength = quotes.length;
quote.innerHTML = quotes[0].quote;
author.innerHTML = quotes[0].author;

nextBtn.addEventListener('click', function () {
    let randomQuote = Math.round(Math.random() * quoteLength);
    if (randomQuote == 7) {
        randomQuote = 1;
    }
    
    let todayQuote = quotes[randomQuote].quote;
    let quoteAuthor = quotes[randomQuote].author;

    let quoteHTML = todayQuote;
    quote.innerHTML = quoteHTML;
    author.innerHTML = quoteAuthor;
});