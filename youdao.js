const crypto = require('crypto');

function _(e) {
    return crypto.createHash("md5").update(e.toString()).digest("hex")
}
function S(e) {

    return _(`client=fanyideskweb&mysticTime=${e}&product=webfanyi&key=SRz6r3IGA6lj9i5zW0OYqgVZOtLDQe3e`)
}
function k() {
        // const a = (new Date).getTime();
         const a='1761142447637'
        return {
            sign: S(a),
            mysticTime: a,
        }
}

console.log(k())