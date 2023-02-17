
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://cdn.discordapp.com/attachments/1045896845785829385/1051985021625434153/Untitled_Artwork.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Censys Search API</h3>
  <p align="center">Need Help?<br/>
    <a href="https://discord.gg/lethals"><strong>Explore the Dscord »</strong></a>
    <br />
    <br />
  </p>
</div>

# About 
Like shodan but better for recon and osint. the censys bots scrape the web looking for all devices even beind protected services like cloudflare then stores them within their database.This allows you to check your host and see if your backend ipaddress is exposed to the public. 

## Setting Up The API:

- Login/Register [Here](https://accounts.censys.io/register).
- Once Register Get Your API ID AND API KEY [Here](https://search.censys.io/account/api).
- Open `Authorization.json` in notepad and/or any text editor.
- API_ID = APP ID | API_KEY = Secret
- Save The File & Run The Script With The Command Below

```cs
python censys.py
```

## Develoeprs:
- Python: 3.10.8
- C# Example [Here](https://github.com/UrFingPoor/CensysAPI)

