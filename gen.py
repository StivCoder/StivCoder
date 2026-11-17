import os, html
# ---- PALETTE: edit here, then re-run `python gen.py` (PROVISIONAL until real site hexes are supplied) ----
P=dict(bg="#0A0A0A",surface="#141414",border="#2A2A2A",primary="#E11D2E",accent="#FFFFFF",text="#FFFFFF",muted="#A3A3A3")
FONT="font-family=\"'Segoe UI',Inter,Helvetica,Arial,sans-serif\""
os.makedirs("assets",exist_ok=True); os.makedirs(".github/workflows",exist_ok=True)
def w(p,s): open(p,"w",encoding="utf-8").write(s)
e=html.escape
defs=f'''<defs>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{P['border']}" stroke-width="1" opacity=".5"/></pattern></defs>'''
def circuits(W,H,n=6):
    paths=[f"M0 {H*.2:.0f}H{W*.12:.0f}L{W*.16:.0f} {H*.1:.0f}H{W*.3:.0f}",
           f"M{W} {H*.25:.0f}H{W*.86:.0f}L{W*.82:.0f} {H*.4:.0f}H{W*.7:.0f}",
           f"M0 {H*.8:.0f}H{W*.1:.0f}L{W*.14:.0f} {H*.9:.0f}H{W*.34:.0f}",
           f"M{W} {H*.78:.0f}H{W*.9:.0f}L{W*.86:.0f} {H*.68:.0f}H{W*.66:.0f}",
           f"M{W*.4:.0f} 0V{H*.08:.0f}L{W*.43:.0f} {H*.14:.0f}H{W*.6:.0f}",
           f"M{W*.5:.0f} {H}V{H*.9:.0f}L{W*.53:.0f} {H*.84:.0f}H{W*.7:.0f}"][:n]
    o=""
    for i,d in enumerate(paths):
        c=P['primary'] if i%2==0 else P['accent']
        o+=f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2" opacity=".25"/>'
        o+=f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2.5" stroke-dasharray="24 300" filter="url(#glow)"><animate attributeName="stroke-dashoffset" from="324" to="0" dur="{3+i*.7:.1f}s" repeatCount="indefinite"/></path>'
    return o
# HEADER
W,H=1200,320
w("assets/header.svg",f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"><title id="t">Stephen Ikumbu Njenga, Software Engineer, Stiv Tech Labs</title><desc id="d">Animated header with circuit lines</desc>{defs}
<rect width="{W}" height="{H}" rx="18" fill="{P['bg']}"/><rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>{circuits(W,H)}
<g {FONT}>
<text x="690" y="70" text-anchor="middle" font-size="16" letter-spacing="6" fill="{P['accent']}">STIV TECH LABS</text>
<text x="690" y="148" text-anchor="middle" font-size="56" font-weight="800" fill="{P['text']}" letter-spacing="2">STEPHEN IKUMBU NJENGA<animate attributeName="opacity" values="0;1" dur="1.2s" fill="freeze"/></text>
<text x="690" y="198" text-anchor="middle" font-size="26" font-weight="700" fill="{P['primary']}" letter-spacing="8">SOFTWARE ENGINEER</text>
<text x="690" y="240" text-anchor="middle" font-size="17" fill="{P['muted']}">Engineering Intelligent Solutions. Building Systems That Matter.</text>
<text x="690" y="282" text-anchor="middle" font-size="15" fill="{P['text']}">🇰🇪 Kenya  •  heartfelt-pony-9fdf85.netlify.app</text></g>
<circle cx="170" cy="160" r="98" fill="none" stroke="{P['primary']}" stroke-width="4"/><circle cx="170" cy="160" r="110" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6 10"><animateTransform attributeName="transform" type="rotate" from="0 170 160" to="360 170 160" dur="20s" repeatCount="indefinite"/></circle>
<clipPath id="pc"><circle cx="170" cy="160" r="92"/></clipPath><image href="data:image/jpeg;base64,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" x="78" y="68" width="184" height="184" clip-path="url(#pc)" preserveAspectRatio="xMidYMid slice"/>
<circle cx="40" cy="300" r="5" fill="{P['primary']}" filter="url(#glow)"><animate attributeName="r" values="4;8;4" dur="2s" repeatCount="indefinite"/></circle>
<circle cx="1160" cy="40" r="5" fill="{P['accent']}" filter="url(#glow)"><animate attributeName="r" values="8;4;8" dur="2s" repeatCount="indefinite"/></circle></svg>''')
# FOOTER
W,H=1200,200
w("assets/footer.svg",f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">Stiv Tech Labs: Engineer minds. Build systems. Create impact.</title>{defs}
<rect width="{W}" height="{H}" rx="18" fill="{P['bg']}"/><rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>{circuits(W,H,4)}
<g {FONT} text-anchor="middle"><text x="600" y="78" font-size="30" font-weight="800" fill="{P['primary']}" letter-spacing="6">STIV TECH LABS</text>
<text x="600" y="116" font-size="17" font-weight="600" fill="{P['text']}" letter-spacing="4">ENGINEER MINDS. BUILD SYSTEMS. CREATE IMPACT.</text>
<text x="600" y="152" font-size="14" fill="{P['muted']}">Clean, Reliable Software for Kenyan Businesses 🇰🇪</text>
<text x="600" y="178" font-size="13" fill="{P['accent']}">heartfelt-pony-9fdf85.netlify.app</text></g></svg>''')
# DIVIDER
W,H=1200,40
w("assets/divider.svg",f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="presentation" aria-hidden="true">{defs}
<path d="M0 20H500L520 8H680L700 20H1200" fill="none" stroke="{P['border']}" stroke-width="2"/>
<path d="M0 20H500L520 8H680L700 20H1200" fill="none" stroke="{P['primary']}" stroke-width="2" stroke-dasharray="60 1140" filter="url(#glow)"><animate attributeName="stroke-dashoffset" from="1200" to="0" dur="5s" repeatCount="indefinite"/></path>
<rect x="592" y="14" width="16" height="16" rx="3" transform="rotate(45 600 22)" fill="{P['accent']}"><animate attributeName="opacity" values=".4;1;.4" dur="2s" repeatCount="indefinite"/></rect></svg>''')
# PROJECT CARDS
def card(fn,icon,name,desc,chips,feats,status,scol):
    W,H=900,300
    ch="";x=40
    for c in chips:
        wd=len(c)*8+24
        ch+=f'<rect x="{x}" y="132" width="{wd}" height="26" rx="13" fill="{P["surface"]}" stroke="{P["primary"]}" stroke-opacity=".6"/><text x="{x+wd/2}" y="150" text-anchor="middle" font-size="12" fill="{P["text"]}">{e(c)}</text>'
        x+=wd+8
    ft="".join(f'<text x="40" y="{190+i*24}" font-size="14" fill="{P["muted"]}"><tspan fill="{P["primary"]}">▸ </tspan>{e(f)}</text>' for i,f in enumerate(feats))
    d="".join(f'<text x="40" y="{92+i*20}" font-size="15" fill="{P["text"]}">{e(l)}</text>' for i,l in enumerate(desc))
    sw=len(status)*8+30
    w("assets/"+fn,f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{e(name)} project card. Status: {e(status)}</title>{defs}
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="{P['bg']}"/><rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="url(#grid)" opacity=".6"/>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="none" stroke="{P['border']}" stroke-width="2"/>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="none" stroke="{P['primary']}" stroke-width="2.5" stroke-dasharray="120 2400" filter="url(#glow)"><animate attributeName="stroke-dashoffset" from="2520" to="0" dur="7s" repeatCount="indefinite"/></rect>
<g {FONT}><text x="40" y="56" font-size="26" font-weight="800" fill="{P['text']}">{icon} {e(name)}</text>
<rect x="{W-sw-40}" y="34" width="{sw}" height="28" rx="14" fill="{scol}" fill-opacity=".15" stroke="{scol}"/><circle cx="{W-sw-24}" cy="48" r="4" fill="{scol}"><animate attributeName="opacity" values="1;.3;1" dur="1.6s" repeatCount="indefinite"/></circle><text x="{W-sw-14}" y="53" font-size="12" font-weight="600" fill="{scol}">{e(status)}</text>
{d}{ch}{ft}</g></svg>''')
card("project-dukapos.svg","🛒","DukaPOS",["Offline-first point-of-sale and retail management app","for Kenyan dukas and small businesses."],
 ["HTML5","CSS3","Vanilla JS (ES Modules)","IndexedDB","esbuild"],
 ["Sales, inventory, transactions, delivery and staff management","Offline-first with local storage, backup/restore and CSV import","Africa/Nairobi timezone handling  •  FastAPI backend planned"],"ACTIVE DEVELOPMENT",P['primary'])
card("project-vectra.svg","⚡","Vectra Tech Portfolio",["A technology services portfolio with a modern,","component-based interface."],
 ["React","TypeScript","Vite"],
 ["Responsive layouts and reusable components","Presents professional technology services","Repository link to be added"],"IN PROGRESS",P['accent'])
card("project-tender-wear.svg","🧸","Terry's Tender Wear",["A live baby-clothing store for a Nairobi client,","with WhatsApp ordering."],
 ["Frontend","Supabase","WhatsApp","M-Pesa"],
 ["Product catalogue, cart and size guide","Cart becomes a WhatsApp order with M-Pesa payment","Admin functionality"],"LIVE (CLIENT WORK)",P['primary'])
w(".github/workflows/snake.yml",'''name: Generate Contribution Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg
            dist/github-snake-dark.svg?palette=github-dark

      - uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
''')
bg,pr,ac,tx=[P[k][1:] for k in("bg","primary","accent","text")]
U="StivCoder"
def icons(ids,label): return f'<img src="https://skillicons.dev/icons?i={ids}&perline=8" alt="{label}"/>'
def badge(t,c=pr): return f'<img src="https://img.shields.io/badge/{t.replace("-","--").replace(" ","_")}-{P["surface"][1:]}?style=for-the-badge&labelColor={P["surface"][1:]}&color={c}" alt="{t}"/>'
README=f'''<div align="center">

<a href="https://heartfelt-pony-9fdf85.netlify.app/"><img src="assets/header.svg" alt="Stephen Ikumbu Njenga, Software Engineer, Stiv Tech Labs" width="100%"/></a>

<img src="https://readme-typing-svg.demolab.com?font=Segoe+UI&weight=600&size=24&pause=1200&color={pr}&center=true&vCenter=true&width=700&lines=Software+Engineer;Full-Stack+Developer;Python+%26+Django+Developer;React+Developer;Flutter+Developer;Building+DukaPOS;Engineering+Business+Solutions;Exploring+Artificial+Intelligence;Turning+Ideas+Into+Software" alt="Rotating headline: Software Engineer, Full-Stack Developer, Python and Django, React, Flutter, building DukaPOS"/>

<br/>

<a href="https://heartfelt-pony-9fdf85.netlify.app/"><img src="https://img.shields.io/badge/🌐_VISIT_MY_PORTFOLIO-STIV_TECH_LABS-{pr}?style=for-the-badge&labelColor={bg}" alt="Visit my portfolio"/></a>
<a href="https://github.com/{U}"><img src="https://img.shields.io/github/followers/{U}?style=for-the-badge&logo=github&labelColor={bg}&color={ac}" alt="GitHub followers"/></a>
<img src="https://komarev.com/ghpvc/?username={U}&style=for-the-badge&label=PROFILE+VIEWS&color={pr}&labelColor={bg}" alt="Profile views"/>

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## 👋 About Me

> *"I don't just build interfaces. I engineer systems that solve real-world problems, simplify operations and create meaningful value."*

Hey! I'm **Stephen**, a **Software Engineer** from Kenya 🇰🇪 passionate about building practical, reliable and scalable software solutions.

I enjoy working across the software development lifecycle: responsive user interfaces, backend systems, database architecture, API development and application logic.

My interests include business automation, AI-powered applications, fintech, cloud engineering and scalable software architecture. Through my engineering work and **Stiv Tech Labs**, I explore how technology can solve practical challenges faced by businesses and institutions.

**Technology should do more than look impressive. It should solve meaningful problems.**

| 🎓 Education | 💼 Experience | 📍 Location | 🏷️ Brand |
|---|---|---|---|
| BSc Software Engineering | 2 years | Kenya 🇰🇪 | Stiv Tech Labs |

<img src="assets/divider.svg" width="100%" alt=""/>

## 🧰 Tech Stack

### ✅ Established skills

<details open>
<summary><b>💻 Programming Languages</b></summary>
<br/>
{icons("py,js,html,css","Python, JavaScript, HTML5, CSS3")}
{badge("SQL")}
</details>

<details>
<summary><b>🎨 Frontend Engineering</b></summary>
<br/>
{icons("react,tailwind,vite,nodejs","React, Tailwind CSS, Vite, Node.js")}
<br/>Responsive interfaces • Component-based architecture • Modern web apps
</details>

<details>
<summary><b>⚙️ Backend Engineering</b></summary>
<br/>
{icons("py,django","Python, Django")}
<br/>REST APIs • Endpoint development • Backend application logic • Application integration
</details>

<details>
<summary><b>📱 Mobile Development</b></summary>
<br/>
{icons("flutter,dart","Flutter, Dart")}
<br/>Cross-platform application development
</details>

<details>
<summary><b>🗄️ Databases and Storage</b></summary>
<br/>
{icons("mongodb,supabase,mysql","MongoDB, Supabase, MySQL")}
{badge("IndexedDB")} {badge("SQL")}
</details>

<details>
<summary><b>🛠️ Developer Tools</b></summary>
<br/>
{icons("git,github,vscode,bash,netlify","Git, GitHub, VS Code, Bash, Netlify")}
{badge("esbuild")} {badge("Automated Testing")}
</details>

### 🔭 Exploring

<details>
<summary><b>🤖 AI and Automation</b></summary>
<br/>
AI • Machine Learning • AI agents • Intelligent business automation<br/><br/>
{badge("n8n",ac)} {badge("Workflow Automation",ac)} {badge("WhatsApp Cloud API",ac)}
</details>

<details>
<summary><b>☁️ Cloud, DevOps and Fintech</b></summary>
<br/>
{icons("azure,githubactions","Microsoft Azure, GitHub Actions")}
{badge("CI/CD",ac)} {badge("DevOps",ac)} {badge("M-Pesa Daraja API",ac)}
</details>

<img src="assets/divider.svg" width="100%" alt=""/>

## 🚀 Featured Projects

<a href="https://github.com/{U}/duka-pos"><img src="assets/project-dukapos.svg" alt="DukaPOS: offline-first point-of-sale for Kenyan dukas. Active development." width="100%"/></a>

**Why it matters:** offline-first architecture keeps a shop trading when the internet drops. Data lives locally in IndexedDB, with backup and restore, so the business never loses a sale to bad connectivity. That is the reality for many Kenyan dukas, and it makes this practical business software rather than a demo.

🔗 [Repository](https://github.com/{U}/duka-pos)

<br/>

<img src="assets/project-vectra.svg" alt="Vectra Tech Portfolio: React, TypeScript and Vite. In progress." width="100%"/>

<br/>

<a href="https://terry-pudding-b23681.netlify.app/"><img src="assets/project-tender-wear.svg" alt="Terry's Tender Wear: live e-commerce store with WhatsApp ordering." width="100%"/></a>

🔗 [Live site](https://terry-pudding-b23681.netlify.app/)

<br/>

### 🏢 Stiv Tech Labs

My broader technology brand: *"Clean, Reliable Software for Kenyan Businesses."* Services include website development, web apps, M-Pesa (Daraja) integration, WhatsApp Cloud API and n8n automation, POS and business systems, REST APIs, UI/UX redesign, graphic design, consulting and AI training. Some of these are active offerings and others are areas I'm still growing into; the portfolio shows what has actually shipped.

🔗 [heartfelt-pony-9fdf85.netlify.app](https://heartfelt-pony-9fdf85.netlify.app/)

### 🌍 More live work

- 🏫 [School Management System](https://stivcoder.github.io/management-school-/): HTML, CSS, JavaScript
- ✨ [Lydian](https://stivcoder.github.io/lydian/): front-end UI showcase in plain HTML, CSS, JavaScript

<img src="assets/divider.svg" width="100%" alt=""/>

## 🧭 My Engineering Journey

I hold a **BSc in Software Engineering** and have **two years** of experience building practical software. My work spans full-stack applications, backend logic, database design, API integration and business automation, and I keep learning by shipping real applications for real businesses.

My long-term ambition: become an engineer who can **design, develop, deploy, scale and maintain** complete software systems, with a growing focus on AI and cloud engineering.

## 🔨 What I'm Building

| Status | Focus |
|---|---|
| 🟢 **Active** | Improving [DukaPOS](https://github.com/{U}/duka-pos) |
| 🟢 **Active** | Building full-stack, practical business applications |
| 🟡 **Learning** | Advanced backend architecture and engineering practices |
| 🟡 **Learning** | Fintech and payment integrations (M-Pesa Daraja) |
| 🔵 **Exploring** | AI integration and cloud infrastructure |

## 💡 Engineering Interests

🤖 AI and Machine Learning • 🧠 AI agents and automation • 💳 Fintech and M-Pesa • 🏢 Enterprise software • ☁️ Cloud and DevOps • 🧱 Scalable backends • 📱 Mobile • 🌍 Digital transformation in Africa

<img src="assets/divider.svg" width="100%" alt=""/>

## 📊 GitHub Stats

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username={U}&show_icons=true&hide_border=true&bg_color={bg}&title_color={pr}&text_color={tx}&icon_color={ac}" alt="GitHub stats"/>
<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username={U}&layout=compact&hide_border=true&bg_color={bg}&title_color={pr}&text_color={tx}" alt="Most used languages"/>

<img src="https://streak-stats.demolab.com?user={U}&hide_border=true&background={bg}&ring={pr}&fire={ac}&currStreakLabel={pr}&sideLabels={tx}&currStreakNum={tx}&sideNums={tx}&dates={P['muted'][1:]}" alt="GitHub streak"/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username={U}&bg_color={bg}&color={tx}&line={pr}&point={ac}&area=true&hide_border=true" alt="Contribution activity graph" width="100%"/>

<img src="https://raw.githubusercontent.com/{U}/{U}/output/github-snake-dark.svg" alt="Contribution snake animation" width="100%"/>

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## 📬 Let's Connect

<div align="center">

<a href="https://heartfelt-pony-9fdf85.netlify.app/"><img src="https://img.shields.io/badge/🌐_Portfolio-{pr}?style=for-the-badge&labelColor={bg}" alt="Portfolio"/></a>
<a href="https://github.com/{U}"><img src="https://img.shields.io/badge/GitHub-{U}-{ac}?style=for-the-badge&logo=github&labelColor={bg}" alt="GitHub"/></a>
<!-- TODO: add your real links, then uncomment
<a href="YOUR_LINKEDIN_URL"><img src="https://img.shields.io/badge/LinkedIn-Connect-{pr}?style=for-the-badge&logo=linkedin&labelColor={bg}" alt="LinkedIn"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-Contact-{ac}?style=for-the-badge&logo=gmail&labelColor={bg}" alt="Email"/></a>
<a href="YOUR_X_URL"><img src="https://img.shields.io/badge/X-Follow-{pr}?style=for-the-badge&logo=x&labelColor={bg}" alt="X"/></a>
-->

</div>

<a href="https://heartfelt-pony-9fdf85.netlify.app/"><img src="assets/footer.svg" alt="Stiv Tech Labs: Engineer minds. Build systems. Create impact." width="100%"/></a>
'''
w("README.md",README)
