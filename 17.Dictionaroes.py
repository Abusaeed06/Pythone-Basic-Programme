monthConversion ={
    "Jan":"January",
    "Feb": "February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",

}
print(monthConversion["Nov"])
print(monthConversion["Jan"])

print(monthConversion.get("Dec"))
print(monthConversion.get("Luv","Not a Valid key"))

# It can also be work properly

monthConversion ={
    1:"January",
    2: "February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December",

}

print(monthConversion[12])