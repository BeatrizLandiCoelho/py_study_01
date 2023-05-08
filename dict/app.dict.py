#_____they hace keys and values

months ={

    "jan":"january",
    "feb":"febuary",
    "mar":"mars",
    "apr":"apryl",
    "may":"may",
    "jun":"June",
    "jl":"July",
    "aul":"algust",
    "set":"setember",
    "oct":"octuber",
    "nov":"november",
    "dez":"dezember"

}

print(months["dez"])

print(months.get("nov"))

#you can pass a second param, the secont param will be the default in case the firt one arent found
print(months.get("abc","default "))