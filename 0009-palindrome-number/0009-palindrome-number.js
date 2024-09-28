/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
        if (x < 0) {
        return false;
    }
     let b = x.toString().split('').reverse().join('');
    if (x === Number(b)) {
        return true;
    } 
    else {
        return false;
    }
};