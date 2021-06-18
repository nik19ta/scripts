function number(num, err) {
    let nums = "1234567890";
    let phone = '';

    if (num[0] == '+') phone = num.substr(1);
    else if (num[0] == "8") phone = num[0] = 7 + num.substr(1);
    else phone = num;

    phone = phone.replace(/\s/g, '');
    phone = phone.replace(/\-/g, '');
    phone = phone.replace(')', '');
    phone = phone.replace('(', '');

    if (phone[0] !== "7") return err;
    if (phone.length !== 11) return err;

    for (let i = 0; i < phone.length; i++) if (nums.indexOf(phone[i]) == -1) return err;

    return phone;
}


const err = "Не верный номер телефона";

console.log(number('+7 800 555 77 78', err)) // 78005557778
console.log(number('+7 800 (555-77-78)', err)) // 78005557778
console.log(number('+7 800 (555-77-78)', err)) // 78005557778
console.log(number('+7 (800) 555-77-78', err)) // 78005557778
console.log(number('8 800 555 77 78', err)) // 78005557778
console.log(number('8 (800) 555-77-78', err)) // 78005557778
console.log(number('8 800 555-77-78', err)) // 78005557778
console.log(number('Err', err)) // Не верный номер телефона
