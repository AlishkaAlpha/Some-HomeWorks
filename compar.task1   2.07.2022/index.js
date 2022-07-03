////////// TASK 1 //////////

/* 

function saniyeler() {
    console.log("5 saniye bitdi dur cix bayira")
}
setTimeout(saniyeler, 5000);
*/

////////// END OF TASK 1 ////////


///////// TASK 2 ///////////

/*
function countDown(a) {
    for (let i = a; i >= 0; i--) {
        console.log(i)
        if (i == 0) {
            console.log("geri sayim bitdi")
        }
    }
}
let number = parseInt(prompt("Enter a number: "));

countDown(number)

*/

///////// END OF TASK 2 ////////


///////// TASK 3 //////////
/*
function result(a) {
    let round = Math.round(a);
    console.log(round)
}
let number = parseFloat(prompt("Enter a Number: "))

console.log(result(number))
*/
///////// END OF TASK 3 ///////

///////// TASK 4 //////////////
/*
function randomizer(max, min) {

    let number = Math.round(Math.random() * (max - min)) + min;
    console.log(number)
}
const max = parseInt(prompt("Enter a Max Value: "))
const min = parseInt(prompt("Enter a Min Value: "))

randomizer(max, min)
*/
/////////// END OF TASK 4 /////////

////////// TASK 5 /////////////
/*
let date = new Date()
let day = date.getDate();
let month = date.getMonth();
let year = date.getFullYear();

let Newdate = (day + "/" + month + "/" + year)


console.log(Newdate)
*/
/////////// END OF TASK 5 /////////////

////////// TASK 6 ////////////
/*
let date = new Date()

let hour = date.getHours();
let minutes = date.getMinutes();
let seconds = date.getSeconds();

let Time = (hour + ":" + minutes + ":" + seconds)

console.log(Time)

*/
////////// END OF TASK 6 /////////////


////////// TASK 7 ////////////
/*


let date = new Date()

let NextYear = new Date(date.getFullYear() + 1, date.getMonth(), date.getDate(), date.getDay(), date.getHours(), date.getMinutes(), date.getSeconds())

console.log(NextYear)
*/
////////// END OF TASK 7 /////////////