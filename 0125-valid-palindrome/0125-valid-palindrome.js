/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let b = s.toLowerCase().replace(/[^a-z0-9]/g, '')
    let c = b.split('').reverse().join('')
    if(b===c){
        return true
    }
    else{
        return false
    }
};