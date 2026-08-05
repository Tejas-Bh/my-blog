---
special: index
---

<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hey, I'm Tejas Bhagawatula.</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* CSS Variables for Accessibility & Light/Dark Theme Switch */
        :root {
            --bg-site: linear-gradient(#1b112b, #0b1c1c) ;
            --card-site: #162032;
            --border-site: #3b4d6b;
            --heading-site: #ffffff;
            --body-site: #f8fafc;
            --subtext-site: #cbd5e1;
            --amber-site: #fbbf24;
            --cyan-site: #38bdf8;
            --phosphor-site: #4ade80;
            --badge-site: #0f172a;
            --header-bg: rgba(2, 6, 23, 0.95);
        }

        html.light {
            --bg-site: #f8fafc;
            --card-site: #ffffff;
            --border-site: #cbd5e1;
            --heading-site: #0f172a;
            --body-site: #1e293b;
            --subtext-site: #475569;
            --amber-site: #d97706;
            --cyan-site: #0284c7;
            --phosphor-site: #15803d;
            --badge-site: #e2e8f0;
            --header-bg: rgba(255, 255, 255, 0.95);
        }

        body {
            background: var(--bg-site);
            color: var(--body-site);
            transition: background-color 0.2s ease, color 0.2s ease;
        }

        .theme-card { background-color: var(--card-site); border-color: var(--border-site); }
        .theme-border { border-color: var(--border-site); }
        .theme-heading { color: var(--heading-site); }
        .theme-subtext { color: var(--subtext-site); }
        .theme-amber { color: var(--amber-site); }
        .theme-cyan { color: var(--cyan-site); }
        .theme-phosphor { color: var(--phosphor-site); }
        .theme-badge { background-color: var(--badge-site); border-color: var(--border-site); }
        .theme-header { background-color: var(--header-bg); border-color: var(--border-site); }
        .theme-text {color: var(--body-site); }
    </style>
</head>
<body class="font-sans text-base leading-relaxed antialiased selection:bg-amber-400 selection:text-slate-950">

    <header class="theme-header border-b-2 sticky top-0 z-50 backdrop-blur-md">
        <div class="max-w-5xl mx-auto px-6 py-4 flex flex-wrap justify-between items-center gap-4">
            <a href="#" class="font-mono text-lg font-bold theme-heading tracking-tight hover:theme-cyan focus:outline-none focus:ring-2 focus:ring-amber-500 rounded px-1 flex items-center gap-2">
                <!-- <span class="w-3 h-3 rounded-full bg-emerald-500 inline-block animate-pulse"></span> -->
                Tejas Bhagawatula
            </a>
            
            <div class="flex items-center gap-4">
                <nav class="flex flex-wrap gap-x-5 gap-y-2 font-mono text-sm font-semibold theme-subtext">
                    <a href="#about" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">#about</a>
                    <a href="{{ link_to('blog') }}" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">/blog</a>
                    <a href="#research" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">#research</a>
                    <a href="#builds" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">#software</a>
                    <a href="#hardware" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">#hardware</a>
                    <a href="#activities" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">#more</a>
                    <a href="#contact" class="hover:theme-amber focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1 transition-colors">#contact</a>
                </nav>

                <button id="theme-toggle" aria-label="Toggle Light and Dark Theme" class="p-2 rounded-lg theme-badge theme-heading hover:theme-cyan border-2 focus:outline-none focus:ring-2 focus:ring-amber-500 transition-colors">
                    <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 100 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
                    <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-6 py-12 space-y-20">

        <section id="about" class="space-y-8 pt-2">
            <div class="space-y-6">
                <h1 class="text-4xl sm:text-5xl font-extrabold tracking-tight theme-heading leading-tight">
                    Exploring signals, software, and the physics of the cosmos.
                </h1>
                <p class="text-lg sm:text-xl leading-relaxed max-w-5xl">
                    I am a high school student passionate about <strong class="theme-heading underline decoration-amber-500 decoration-2">embedded systems, signal processing, astrophysics, and open-source engineering</strong>. 
                    My primary aspiration is to <strong class="theme-heading">explore the intersection between physics and electronics</strong> while developing accessible tools for scientific computing and radio observation.
                </p>
                <p class="theme-subtext text-base sm:text-lg leading-relaxed max-w-5xl">
                    Whether I'm analyzing spectral data, constructing custom software utilities on Linux, practicing radio telemetry, or playing classical instruments, I enjoy discovering how complex mathematical and physical systems fit together.
                </p>
            </div>

            <div class="theme-card border-2 rounded-xl p-6 font-mono text-sm space-y-4 shadow-md">
                <div class="flex flex-wrap justify-between items-center theme-amber font-bold text-base border-b theme-border pb-3 gap-2">
                    <span>Who is KJ5OAE (my amateur radio callsign)?</span>
                    <!-- <span class="theme-subtext font-normal text-xs theme-badge border px-2.5 py-1 rounded">FCC Licensed Amateur Radio Operator</span> -->
                </div>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 theme-subtext">
                    <div>
                        <span class="theme-heading block font-bold text-base mb-0.5">Location / Grid:</span>
                        <span>Austin, Texas (EM10)</span>
                    </div>
                    <div>
                        <span class="theme-heading block font-bold text-base mb-0.5">Primary Focus:</span>
                        <span>Embedded Software, Radio Astronomy & Signal Analysis</span>
                    </div>
                    <div>
                        <span class="theme-heading block font-bold text-base mb-0.5">Musical Instruments:</span>
                        <span>Violin, Viola, Guitar, Voice</span>
                    </div>
                    <div>
                        <span class="theme-heading block font-bold text-base mb-0.5">Core Hobbies:</span>
                        <span>Origami, Linux Customization, Ham Radio, Desmos Math Art</span>
                    </div>
                </div>
            </div>
        </section>

        <section id="research" class="space-y-6 scroll-mt-24">
            <div class="border-b-2 theme-border pb-4">
                <h2 class="text-2xl sm:text-3xl font-extrabold theme-heading flex items-center gap-3 underline decoration-amber-500 decoration-2">
                  <!--<span class="theme-amber  text-xl sm:text-2xl">01.</span>--> Investigations
                </h2>
                <p class="theme-subtext text-base mt-1">Opportunistic atmospheric sensing, ionospheric sounding, and novel computing architectures!</p>
            </div>

                <div class="theme-card border-2 p-5 rounded-xl text-sm theme-subtext space-y-2">
                    <span class="theme-heading font-bold text-base block">Academic & Scientific Working Groups:</span>
                    <ul class="list-disc list-inside space-y-1 font-mono text-xs sm:text-sm">
                        <li><strong>HamSCI HF Channel Sounding Working Group:</strong> Lead developer on <code class="theme-amber">wsjt-probe</code> channel sounder.</li>
                        <li><strong>HamSCI K-12 Curricular Integration Group:</strong> Contributing to the development of a curriculum for the Personal Space Weather Station (PSWS).</li>
                    </ul>
                </div>
 

            <div class="space-y-6">
                <div class="theme-card border-2 p-6 rounded-xl space-y-4 hover:border-sky-400 transition-colors">
                    <div class="flex flex-wrap justify-between items-start gap-2">
                        <div>
                            <!--<span class="text-s theme-amber font-bold tracking-wider block mb-1"><i>HamSCI HF Channel Sounding Working Group</i></span>-->
                            <h3 class="font-bold theme-heading text-xl">FT8 Opportunistic Ionospheric Sounding (<code class="text-sky-400">wsjt-probe</code>)</h3>
                        </div>
                        <a href="https://github.com/Tejas-Bh/wsjt-probe" target="_blank" class="text-sm font-mono font-bold theme-cyan hover:underline border theme-border theme-badge px-3 py-1 rounded">>GitHub Repo<</a>
                    </div>
                    <p class="text-sm sm:text-base theme-subtext leading-relaxed">
                        Invented a novel method for opportunistic atmospheric sensing using open-source amateur FT8 radio signals. Unlike traditional broad observables, this protocol reconstructs received signals to perform waveform-level comparisons directly on the receiver end, eliminating the need to store massive I/Q datasets.
                    </p>
                    <div class="text-xs theme-subtext border-t theme-border pt-3 flex flex-wrap justify-between items-center gap-2">
                        <span class="theme-cyan font-bold">In Progress: Verifying on-the-air data & collaborating with HamSCI for international PSWS deployment.</span>
                        <span class="theme-badge border px-2 py-0.5 rounded">C++ / Python / Signal Processing</span>
                    </div>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-4 hover:border-sky-400 transition-colors">
                    <div class="flex flex-wrap justify-between items-start gap-2">
                        <div>
                            <!-- <span class="text-xs font-mono theme-amber font-bold uppercase tracking-wider block mb-1">Independent Research</span> -->
                            <h3 class="font-bold theme-heading text-xl">Wireless Signal Neuromorphic Architecture (<code class="text-sky-400">neurodft</code>)</h3>
                        </div>
                        <a href="https://github.com/Tejas-Bh/neurodft" target="_blank" class="text-sm font-mono font-bold theme-cyan hover:underline border theme-border theme-badge px-3 py-1 rounded">>GitHub Repo<</a>
                    </div>
                    <p class="text-sm sm:text-base theme-subtext leading-relaxed">
                        Independently conceptualized and developed a neuromorphic computing model using wireless signal properties. Demonstrates auto-associative memory with routing complexity significantly reduced compared to standard industry baselines.
                    </p>
                    <div class="text-xs theme-subtext border-t theme-border pt-3 flex flex-wrap justify-between items-center gap-2">
                        <!-- <span class="theme-cyan font-bold">Focus: Auto-Associative Memory & Waveform Routing</span> -->
                        <span class="theme-badge border px-2 py-0.5 rounded">Python / Neuromorphic Computing</span>
                    </div>
                </div>

           </div>
        </section>

        <section id="builds" class="space-y-6 scroll-mt-24">
            <div class="border-b-2 theme-border pb-4">
                <h2 class="text-2xl sm:text-3xl font-extrabold theme-heading flex items-center gap-3 underline decoration-amber-500 decoration-2">
                    <!--<span class="theme-amber text-xl sm:text-2xl">02.</span> -->Software & Web Engineering
                </h2>
                <p class="theme-subtext text-base mt-1">Audio processing tools, web frameworks, Linux operating systems, and automation utilities.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="theme-card border-2 p-6 rounded-xl space-y-3">
                    <div class="flex justify-between items-center gap-2">
                        <h3 class="font-bold theme-heading text-lg">mediaplayer-generator</h3>
                        <a href="https://github.com/Tejas-Bh/mediaplayer-generator" target="_blank" class="text-xs font-mono font-bold theme-cyan hover:underline">>GitHub<</a>
                    </div>
                    <p class="text-sm theme-subtext leading-relaxed">
                        Audio processing utility that generates performance interfaces and applies gain control and audio balancing algorithms. Utilized in 20+ live shows across the Austin area.
                    </p>
                    <div class="flex flex-wrap gap-1.5 pt-2">
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Audio DSP</span>
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Python</span>
                    </div>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-3">
                    <div class="flex justify-between items-center gap-2">
                        <h3 class="font-bold theme-heading text-lg">fsp (Flask Pages)</h3>
                        <a href="https://github.com/Tejas-Bh/fsp" target="_blank" class="text-xs font-mono font-bold theme-cyan hover:underline">>GitHub<</a>
                    </div>
                    <p class="text-sm theme-subtext leading-relaxed">
                        A lightweight site generator written in Flask that enables the rapid generation of feature-rich static and dynamic web pages with minimal HTML markup writing.
                    </p>
                    <div class="flex flex-wrap gap-1.5 pt-2">
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Flask</span>
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Python / Web</span>
                    </div>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-3">
                    <div class="flex justify-between items-center gap-2">
                        <h3 class="font-bold theme-heading text-lg">Podwave</h3>
                        <span class="text-xs font-mono theme-subtext">Deployment in progress!</span>
                    </div>
                    <p class="text-sm theme-subtext leading-relaxed">
                        React application interfacing with a locally hosted Ollama LLM to transform news articles into podcast-style summaries via asynchronous frontend API calls.
                    </p>
                    <div class="flex flex-wrap gap-1.5 pt-2">
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">React</span>
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Ollama API</span>
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">LLM</span>
                    </div>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-3">
                    <div class="flex justify-between items-center gap-2">
                        <h3 class="font-bold theme-heading text-lg">VoxOS</h3>
                        <span class="text-xs font-mono theme-subtext">Linux Distribution</span>
                    </div>
                    <p class="text-sm theme-subtext leading-relaxed">
                        A custom Linux-based operating system distribution tailored specifically for audio and video media engineering professionals.
                    </p>
                    <div class="flex flex-wrap gap-1.5 pt-2">
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Linux OS</span>
                        <span class="text-xs font-mono theme-badge px-2.5 py-0.5 rounded border">Shell Scripting</span>
                    </div>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-3 md:col-span-2">
                    <h3 class="font-bold theme-heading text-lg">Infrastructure Automation Tools</h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm theme-subtext pt-1">
                        <div class="space-y-1 border-l-2 theme-border pl-3">
                            <h4 class="font-bold theme-heading">Flask-Aht-Tickets</h4>
                            <p class="text-xs">Flask ticket management web app supporting maintenance requests, project tracking, and simplified issue workflows.</p>
                            <p class="text-xs underline theme-cyan font-bold"><a href="https://maintenance.austinhindutemple.org">Official Website</a></p>
                        </div>
                        <div class="space-y-1 border-l-2 theme-border pl-3">
                            <h4 class="font-bold theme-heading">aht-kiosk Automation</h4>
                            <p class="text-xs">Automated digital signage system connecting Google Drive with Python, PowerShell, and Batch scripts for nontechnical users.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="hardware" class="space-y-6 scroll-mt-24">
            <div class="border-b-2 theme-border pb-4">
                <h2 class="text-2xl sm:text-3xl font-extrabold theme-heading flex items-center gap-3 underline decoration-amber-500 decoration-2">
                    <!--<span class="theme-amber text-xl sm:text-2xl">03.</span>--> Electronics, Robotics & Radio
                </h2>
                <p class="theme-subtext text-base mt-1">Autonomous vehicles, microcontroller firmware, and radio station builds.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="theme-card border-2 p-6 rounded-xl space-y-3">
                    <div class="flex justify-between items-start gap-2">
                        <h3 class="font-bold theme-heading text-lg">Science Olympiad Autonomous EV</h3>
                        <!-- <span class="text-xs font-mono font-bold theme-amber bg-slate-900 border theme-border px-2 py-0.5 rounded">1st Place Regionals</span> -->
                    </div>
                    <p class="text-sm theme-subtext leading-relaxed">
                        Designed and built an autonomous navigation vehicle utilizing an Arduino Nano 33 BLE and custom C++ PID control loops for precise target distance and braking timing calculations.
                    </p>
                    <div class="text-xs font-mono theme-subtext pt-1">
                        Tools: C++, PID Control, Microcontrollers, CAD & Fabrication
                    </div>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-3">
                    <div class="flex justify-between items-start gap-2">
                        <h3 class="font-bold theme-heading text-lg">KJ5OAE RF Receiver Hardware</h3>
                        <!-- <span class="text-xs font-mono font-bold theme-cyan bg-slate-900 border theme-border px-2 py-0.5 rounded">Station Gear</span> -->
                    </div>
                    <p class="text-sm theme-subtext leading-relaxed">
                        Hardware deployment and antenna tuning for <code class="theme-amber">wsjt-probe</code> data collection, packet telemetry reception, and tropospheric ducting monitoring over VHF/UHF frequencies.
                    </p>
                    <div class="text-xs font-mono theme-subtext pt-1">
                        Tools: RTL-SDR, Dipoles, NEC, Handheld Transceivers
                    </div>
                </div>
            </div>
        </section>

        <section id="activities" class="space-y-6 scroll-mt-24">
            <div class="border-b-2 theme-border pb-4">
                <h2 class="text-2xl sm:text-3xl font-extrabold theme-heading flex items-center gap-3 underline decoration-amber-500 decoration-2">
                    <!--<span class="theme-amber text-xl sm:text-2xl">04.</span>--> Music, Science & Creative Pursuits
                </h2>
                 <p class="theme-subtext text-base mt-1">Useful exercises that are also fun!</p> 
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="theme-card border-2 p-6 rounded-xl space-y-2">
                    <h3 class="font-bold theme-heading text-lg">Music & Vocal Performance</h3>
                    <p class="text-xs sm:text-sm theme-subtext leading-relaxed">
                        Playing the <strong class="theme-heading">Violin, Viola, Guitar, and Voice</strong>. Music has been a great way to explore my creativity, improve my discipline, and make new friends.
                    </p>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-2">
                    <h3 class="font-bold theme-heading text-lg">Science Olympiad</h3>
                    <p class="text-xs sm:text-sm theme-subtext leading-relaxed">
                        Competitor and <b>test writer</b> focusing on Astronomy, Remote Sensing, Autonomous Vehicles, and Physics competitions.
                    </p>
                </div>

                <div class="theme-card border-2 p-6 rounded-xl space-y-2">
                    <h3 class="font-bold theme-heading text-lg">Origami & Desmos Math Art</h3>
                    <p class="text-xs sm:text-sm theme-subtext leading-relaxed">
                        Designing modular geometric origami and plotting mathematical equation art in Desmos, combining spatial geometry with design.
                    </p>
                </div>
            </div>
        </section>

        <section id="blog" class="space-y-6 scroll-mt-24">
            <div class="border-b-2 theme-border pb-4 flex flex-wrap justify-between items-end gap-2">
                <div>
                    <h2 class="text-2xl sm:text-3xl font-extrabold theme-heading flex items-center gap-3 underline decoration-amber-500 decoration-2">
                        <!--<span class="theme-amber text-xl sm:text-2xl">05.</span>--> Blog & Workbench Notes
                    </h2>
                    <p class="theme-subtext text-base mt-1">Technical write-ups, radio logs, music, and any other things I find fascinating.</p>
                </div>
            </div>

            <div class="space-y-6">
            {% for post in scripts.get_posts()[:3] %}
                <article class="theme-card border-2 p-6 rounded-xl space-y-3 hover:border-amber-400 transition-colors">
                    <div class="flex flex-wrap justify-between items-center gap-2 text-xs font-mono theme-subtext">
                        <span class="theme-amber font-bold">{{ post[2] }}</span>
                    </div>
                    <h3 class="text-xl font-bold theme-heading hover:theme-cyan">
                        <a href="{{ link_to(post[0]) }}" class="focus:outline-none focus:underline">{{ post[1] }}</a>
                    </h3>
                    <p class="text-sm theme-subtext leading-relaxed">
                        {{ post[3] }}
                    </p>
                    <div class="pt-1">
                        <a href="{{ link_to(post[0]) }}" class="text-sm font-bold theme-cyan hover:underline inline-flex items-center gap-1">Read Article</a>
                    </div>
                </article>
            {% endfor %}
            <p><a href="{{ link_to('blog') }}" class="text-sm font-bold theme-cyan hover:underline inline-flex items-center gap-1">View all my posts &#9654;
        <footer id="contact" class="border-t-2 theme-border pt-10 pb-16 space-y-6 font-mono text-sm">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6">
                <div class="space-y-2">
                    <p class="theme-heading font-bold text-base">Get in touch! I'd love to talk.</p>
                    <p class="theme-amber font-bold text-base theme-badge border px-3 py-1.5 rounded inline-block">
                        tejas.bhagawatula [at] gmail [dot] com
                    </p>
                </div>
                <div class="flex items-center space-x-6 text-base font-bold">
                    <a href="https://github.com/Tejas-Bh/" target="_blank" class="theme-cyan hover:underline focus:outline-none focus:ring-1 focus:ring-amber-500 rounded px-1">GitHub</a>
                </div>
            </div>
            <div class="theme-subtext text-xs flex flex-wrap justify-between items-center border-t theme-border pt-6 gap-2">
                <span class="font-bold theme-heading">&copy; Tejas Bhagawatula. 73 DE KJ5OAE!</span>
                <span>Built with Tailwind CSS, Flask, AWS, and love.</span>
            </div>
        </footer>

    </main>

    <script>
        const themeToggleBtn = document.getElementById('theme-toggle');
        const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
        const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

        if (localStorage.getItem('color-theme') === 'light' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: light)').matches)) {
            document.documentElement.classList.add('light');
            document.documentElement.classList.remove('dark');
            themeToggleDarkIcon.classList.remove('hidden');
        } else {
            document.documentElement.classList.add('dark');
            document.documentElement.classList.remove('light');
            themeToggleLightIcon.classList.remove('hidden');
        }

        themeToggleBtn.addEventListener('click', function() {
            themeToggleDarkIcon.classList.toggle('hidden');
            themeToggleLightIcon.classList.toggle('hidden');

            if (document.documentElement.classList.contains('light')) {
                document.documentElement.classList.remove('light');
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            } else {
                document.documentElement.classList.remove('dark');
                document.documentElement.classList.add('light');
                localStorage.setItem('color-theme', 'light');
            }
        });
    </script>
</body>
</html>
