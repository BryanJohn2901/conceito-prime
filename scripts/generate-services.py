#!/usr/bin/env python3
import os, shutil, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVICES = [
    {
        "slug": "redes-sociais",
        "title": "Redes Sociais",
        "icon": "fa-share-nodes",
        "icon_lib": "fas",
        "tagline": "Presença digital com curadoria e estratégia",
        "summary": "Curadoria, posicionamento e gestão de redes para conexões profundas e autênticas.",
        "intro": "Transformamos suas redes sociais em um canal estratégico de relacionamento e conversão. Criamos conteúdo com identidade visual alinhada à sua marca, planejamos calendários editoriais e monitoramos métricas para evolução contínua.",
        "benefits": [
            ("Posicionamento de marca", "Construímos uma presença coerente que transmite autoridade e proximidade com seu público."),
            ("Conteúdo estratégico", "Posts, stories e reels pensados para engajar e converter, não apenas para preencher feed."),
            ("Gestão completa", "Planejamento, produção, publicação e relatórios mensais com análise de desempenho."),
            ("Comunidade ativa", "Interação humanizada que fortalece o vínculo entre marca e seguidores."),
        ],
        "includes": [
            "Diagnóstico de perfil e concorrência",
            "Calendário editorial mensal",
            "Criação de artes e copy",
            "Gestão de Instagram, Facebook e LinkedIn",
            "Relatório de métricas e insights",
        ],
        "image_src": "assets/images/portfolio/portfolio-01.webp",
        "image_alt": "Projeto de social media da Conceito Prime",
    },
    {
        "slug": "google-meta-ads",
        "title": "Google e Meta Ads",
        "icon": "fa-google",
        "icon_lib": "fab",
        "tagline": "Tráfego pago com inteligência e ROI",
        "summary": "Inteligência de tráfego pago focado na atração de público qualificado de alto valor.",
        "intro": "Campanhas de mídia paga estruturadas para atrair leads e vendas com previsibilidade. Trabalhamos com Google Ads, Meta Ads e remarketing, otimizando investimento e ampliando o alcance da sua marca junto ao público certo.",
        "benefits": [
            ("Público qualificado", "Segmentação avançada para alcançar quem realmente tem interesse no seu produto ou serviço."),
            ("Otimização contínua", "Testes A/B, ajustes de lance e criativos para maximizar retorno sobre investimento."),
            ("Rastreamento preciso", "Configuração de pixels, conversões e funis para medir cada etapa da jornada."),
            ("Escalabilidade", "Estratégias que crescem junto com o seu negócio, do lançamento à consolidação."),
        ],
        "includes": [
            "Auditoria de contas e estrutura de campanhas",
            "Criação e gestão de anúncios Google e Meta",
            "Configuração de conversões e pixels",
            "Relatórios semanais de performance",
            "Reuniões de alinhamento estratégico",
        ],
        "image_src": "assets/images/portfolio/portfolio-02.webp",
        "image_alt": "Campanha de mídia paga gerenciada pela Conceito Prime",
    },
    {
        "slug": "plataformas-web",
        "title": "Plataformas Web",
        "icon": "fa-laptop-code",
        "icon_lib": "fas",
        "tagline": "Sites que convertem visitantes em clientes",
        "summary": "Desenvolvimento de sites institucionais com design minimalista e altíssima conversão.",
        "intro": "Desenvolvemos sites institucionais e landing pages com foco em performance, SEO e experiência do usuário. Cada projeto é pensado para representar sua marca com elegância e gerar resultados mensuráveis.",
        "benefits": [
            ("Design sob medida", "Layout exclusivo alinhado ao manual de marca e identidade visual."),
            ("Alta performance", "Páginas rápidas, responsivas e otimizadas para buscadores."),
            ("Conversão", "Estrutura de conteúdo e CTAs estratégicos para captar leads."),
            ("Manutenção", "Suporte técnico e atualizações para manter seu site sempre atual."),
        ],
        "includes": [
            "Briefing e wireframe estratégico",
            "Design UI/UX responsivo",
            "Desenvolvimento HTML/CSS/JS otimizado",
            "Integração com formulários e analytics",
            "SEO técnico on-page",
        ],
        "image_src": "assets/images/portfolio/portfolio-02.webp",
        "image_alt": "Projeto de web design da Conceito Prime",
    },
    {
        "slug": "papelaria-fina",
        "title": "Papelaria Fina",
        "icon": "fa-file-invoice",
        "icon_lib": "fas",
        "tagline": "Materiais impressos com requinte e credibilidade",
        "summary": "Design de materiais impressos que transmitem credibilidade e requinte absoluto.",
        "intro": "Cartões de visita, folders, apresentações e materiais corporativos que reforçam a percepção de valor da sua marca. Cada peça é desenvolvida com atenção à tipografia, cores e acabamentos premium.",
        "benefits": [
            ("Identidade consistente", "Todos os materiais seguem o manual de marca da empresa."),
            ("Acabamento premium", "Sugestões de papel, verniz e cortes especiais para impacto visual."),
            ("Arquivos prontos", "Entrega em formatos adequados para gráficas e fornecedores."),
            ("Versatilidade", "Do cartão de visita ao folder institucional completo."),
        ],
        "includes": [
            "Cartões de visita e papel timbrado",
            "Folders e apresentações institucionais",
            "Envelopes e materiais de escritório",
            "Arquivos CMYK para impressão",
            "Acompanhamento na produção gráfica",
        ],
        "image_src": "assets/images/portfolio/portfolio-04.webp",
        "image_alt": "Projeto de papelaria corporativa da Conceito Prime",
    },
    {
        "slug": "branding",
        "title": "Branding",
        "icon": "fa-lightbulb",
        "icon_lib": "fas",
        "tagline": "Marcas memoráveis com propósito claro",
        "summary": "Construção e reposicionamento de marcas voltadas para o segmento de luxo.",
        "intro": "Criamos e reposicionamos marcas com estratégia, narrativa e identidade visual completa. Do naming à aplicação em todos os pontos de contato, garantimos que sua marca se destaque com personalidade e consistência.",
        "benefits": [
            ("Posicionamento claro", "Definição de tom de voz, valores e diferenciais competitivos."),
            ("Identidade visual", "Logotipo, paleta de cores, tipografia e elementos gráficos."),
            ("Manual de marca", "Documento completo para uso consistente em todos os canais."),
            ("Reposicionamento", "Estratégia para marcas que precisam se reinventar no mercado."),
        ],
        "includes": [
            "Pesquisa de mercado e benchmarking",
            "Desenvolvimento de logotipo e variações",
            "Paleta de cores e tipografia",
            "Manual de identidade visual",
            "Aplicações em mockups e materiais",
        ],
        "image_src": "assets/images/portfolio/portfolio-06.webp",
        "image_alt": "Projeto de branding corporativo da Conceito Prime",
    },
    {
        "slug": "treinamentos",
        "title": "Treinamentos",
        "icon": "fa-chalkboard-user",
        "icon_lib": "fas",
        "tagline": "Capacitação que eleva o padrão do time",
        "summary": "Capacitação in-company focada em atendimento primoroso e excelência relacional.",
        "intro": "Programas de treinamento personalizados para equipes comerciais, de atendimento e liderança. Conteúdo prático, dinâmico e alinhado aos desafios reais do seu negócio.",
        "benefits": [
            ("Conteúdo customizado", "Módulos adaptados ao perfil e necessidades da sua equipe."),
            ("Metodologia prática", "Dinâmicas, role-play e estudos de caso para fixação."),
            ("Resultados mensuráveis", "Indicadores antes e depois para avaliar evolução."),
            ("Certificação", "Reconhecimento formal da participação dos colaboradores."),
        ],
        "includes": [
            "Diagnóstico de necessidades da equipe",
            "Material didático exclusivo",
            "Workshops presenciais ou online",
            "Avaliação de desempenho pós-treinamento",
            "Suporte pós-entrega por 30 dias",
        ],
        "image_src": "assets/images/estrutura.webp",
        "image_alt": "Equipe em treinamento na Conceito Prime",
    },
    {
        "slug": "pesquisa-dados",
        "title": "Pesquisa & Dados",
        "icon": "fa-chart-line",
        "icon_lib": "fas",
        "tagline": "Decisões baseadas em evidências reais",
        "summary": "Levantamento de percepção de valor e satisfação para refinamento contínuo.",
        "intro": "Pesquisas de satisfação, NPS, percepção de marca e análise de dados para embasar decisões estratégicas. Transformamos feedback em planos de ação concretos.",
        "benefits": [
            ("Visão do cliente", "Entenda o que seu público pensa, sente e espera da sua marca."),
            ("Benchmarking", "Compare seu desempenho com referências do setor."),
            ("Insights acionáveis", "Relatórios claros com recomendações práticas."),
            ("Monitoramento", "Acompanhamento periódico para medir evolução ao longo do tempo."),
        ],
        "includes": [
            "Desenho de questionários e metodologia",
            "Coleta online ou presencial",
            "Análise estatística dos resultados",
            "Relatório executivo com insights",
            "Plano de ação recomendado",
        ],
        "image_src": "assets/images/portfolio/portfolio-03.webp",
        "image_alt": "Análise de dados e pesquisa de mercado",
    },
    {
        "slug": "automacao-vip",
        "title": "Automação VIP",
        "icon": "fa-whatsapp",
        "icon_lib": "fab",
        "tagline": "Atendimento inteligente com toque humano",
        "summary": "Arquitetura de atendimento otimizado no WhatsApp mantendo o toque humano.",
        "intro": "Fluxos automatizados no WhatsApp Business que qualificam leads, respondem dúvidas frequentes e encaminham oportunidades para sua equipe — sem perder a personalização que seu cliente espera.",
        "benefits": [
            ("Resposta imediata", "Atendimento 24/7 para dúvidas e solicitações iniciais."),
            ("Qualificação de leads", "Fluxos que identificam o perfil e a intenção do contato."),
            ("Integração com CRM", "Dados organizados para follow-up eficiente da equipe comercial."),
            ("Experiência premium", "Mensagens personalizadas que refletem o padrão da sua marca."),
        ],
        "includes": [
            "Mapeamento de jornada do cliente",
            "Configuração do WhatsApp Business API",
            "Criação de fluxos e respostas automáticas",
            "Integração com ferramentas de gestão",
            "Treinamento da equipe de atendimento",
        ],
        "image_src": "assets/images/portfolio/portfolio-05.webp",
        "image_alt": "Automação de atendimento via WhatsApp",
    },
]


def render_footer(title):
    return f'''
  <section class="bg-prime-950 py-20">
    <div class="max-w-3xl mx-auto px-6 lg:px-8 text-center">
      <span class="inline-block border border-gold-400/30 text-gold-400 font-bold tracking-widest uppercase text-xs px-5 py-2 rounded-full mb-6">#SejaPrime</span>
      <h2 class="text-3xl sm:text-4xl font-serif text-white mb-5 uppercase">Vamos conversar?</h2>
      <p class="text-white/60 mb-8 leading-relaxed">Solicite um orçamento personalizado para <strong class="text-gold-400">{title}</strong> e descubra como podemos impulsionar seus resultados.</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/contato/" class="btn-brand inline-flex items-center justify-center gap-2 px-8 py-4 uppercase tracking-[0.2em] text-[11px]">Solicitar orçamento</a>
        <a href="https://wa.me/554130574764" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2 border border-white/20 hover:border-white text-white font-semibold px-8 py-4 transition-all text-sm"><i class="fab fa-whatsapp"></i> WhatsApp</a>
      </div>
    </div>
  </section>
  </main>

  <footer class="bg-prime-950 pt-24 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <div class="grid lg:grid-cols-12 gap-12 lg:gap-8 mb-20 items-start border-b border-white/10 pb-20">
        <div class="lg:col-span-5">
          <img src="../../assets/images/logo.webp" alt="Conceito Prime - Marketing Digital" width="400" height="114" class="h-8 object-contain mb-8 filter brightness-0 invert opacity-90">
          <p class="text-prime-400 font-light text-[13px] leading-[1.8] max-w-sm">Especialistas em posicionamento, branding e tráfego para marcas que buscam autoridade e resultados de altíssimo padrão.</p>
        </div>
        <div class="lg:col-span-3 lg:col-start-7">
          <h2 class="text-white font-serif text-lg mb-6">Menu</h2>
          <ul class="space-y-4">
            <li><a href="/" class="text-prime-400 hover:text-gold-400 transition text-[13px] font-light">Início</a></li>
            <li><a href="/quem-somos/" class="text-prime-400 hover:text-gold-400 transition text-[13px] font-light">A Agência</a></li>
            <li><a href="/blog/" class="text-prime-400 hover:text-gold-400 transition text-[13px] font-light">Journal</a></li>
            <li><a href="/contato/" class="text-prime-400 hover:text-gold-400 transition text-[13px] font-light">Contato</a></li>
          </ul>
        </div>
        <div class="lg:col-span-3">
          <h2 class="text-white font-serif text-lg mb-6">Social</h2>
          <div class="flex gap-4">
            <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:border-gold-400 hover:text-gold-400 transition-all duration-300" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:border-gold-400 hover:text-gold-400 transition-all duration-300" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
          </div>
        </div>
      </div>
      <div class="flex flex-col md:flex-row justify-between items-center gap-6 text-[11px] text-prime-500 uppercase tracking-widest font-light">
        <p>© 2026 Conceito Prime.</p>
        <p>Design & Code por Conceito Prime</p>
      </div>
    </div>
  </footer>
  <script>
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    menuBtn.addEventListener('click', () => {{
      mobileMenu.classList.toggle('hidden');
      const icon = menuBtn.querySelector('i');
      icon.classList.toggle('fa-bars');
      icon.classList.toggle('fa-times');
    }});
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 20));
  </script>
</body>
</html>'''


def render_head(svc, schema):
    s = svc
    return f'''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s['title']} | Conceito Prime</title>
  <link rel="canonical" href="https://conceitop.com.br/servicos/{s['slug']}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{s['title']} | Conceito Prime">
  <meta property="og:description" content="{s['summary']}">
  <meta property="og:url" content="https://conceitop.com.br/servicos/{s['slug']}/">
  <meta name="robots" content="index, follow">
  <meta name="description" content="{s['summary']}">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800&family=Share+Tech&family=Michroma&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="../../assets/css/brand.css">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Cairo', 'sans-serif'],
            serif: ['Tachyon', 'Share Tech', 'sans-serif'],
            display: ['Cosild', 'Michroma', 'sans-serif']
          }},
          colors: {{
            prime: {{ 50:'#fafafa', 100:'#f0f0f0', 200:'#d9d9d9', 300:'#a3a3a3', 400:'#6b6b6b', 500:'#4a4a4a', 600:'#353535', 700:'#2a2a2a', 800:'#1f1f1f', 900:'#161616', 950:'#0d0d0d' }},
            gold:  {{ 300:'#fce88a', 400:'#f7cc19', 500:'#e5b800', 600:'#c9a000' }},
            accent: {{ DEFAULT:'#ff4c01', light:'#ff7a3d', pale:'#ffd4b8' }}
          }}
        }}
      }}
    }}
  </script>
  <script type="application/ld+json">{schema}</script>
</head>
<body class="font-sans text-prime-800 antialiased">

  <header id="header" class="fixed inset-x-0 top-0 z-50 py-4">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <nav class="flex items-center justify-between" aria-label="Navegação principal">
        <a href="/" class="flex items-center h-10">
          <img src="../../assets/images/logo.webp" alt="Conceito Prime - Marketing Digital" width="400" height="114" class="h-full object-contain">
        </a>
        <div class="hidden md:flex items-center gap-10">
          <a href="/" class="nav-link text-prime-900 text-[13px] uppercase tracking-widest font-medium transition">Início</a>
          <a href="/quem-somos/" class="nav-link text-prime-900 text-[13px] uppercase tracking-widest font-medium transition">Quem somos</a>
          <a href="/blog/" class="nav-link text-prime-900 text-[13px] uppercase tracking-widest font-medium transition">Blog</a>
          <a href="/contato/" class="nav-link text-prime-900 text-[13px] uppercase tracking-widest font-medium transition">Contato</a>
        </div>
        <div class="flex items-center gap-4">
          <a href="/contato/" class="hidden md:inline-flex items-center justify-center bg-prime-900 text-white font-semibold text-[11px] px-7 py-3 rounded-none uppercase tracking-[0.2em] hover:bg-accent transition-all duration-300">Orçamento Rápido</a>
          <button id="menu-btn" type="button" aria-label="Abrir menu" aria-expanded="false" class="md:hidden text-prime-900 focus:outline-none"><i class="fas fa-bars text-xl"></i></button>
        </div>
      </nav>
      <div id="mobile-menu" class="hidden md:hidden mt-4 pb-4 border-t border-gray-100 pt-4 flex flex-col gap-4 bg-white/95">
        <a href="/" class="text-prime-900 text-sm uppercase tracking-widest font-medium transition px-2">Início</a>
        <a href="/quem-somos/" class="text-prime-900 text-sm uppercase tracking-widest font-medium transition px-2">Quem somos</a>
        <a href="/blog/" class="text-prime-900 text-sm uppercase tracking-widest font-medium transition px-2">Blog</a>
        <a href="/contato/" class="text-prime-900 text-sm uppercase tracking-widest font-medium transition px-2">Contato</a>
        <a href="/contato/" class="inline-flex justify-center items-center bg-prime-900 text-white font-medium text-xs px-6 py-4 mt-2 uppercase tracking-[0.2em]">Orçamento Rápido</a>
      </div>
    </div>
  </header>

  <main>
  <nav aria-label="Breadcrumb" class="pt-28 pb-4 bg-prime-50">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <ol class="flex flex-wrap items-center gap-2 text-[11px] uppercase tracking-widest text-prime-500">
        <li><a href="/" class="hover:text-gold-500 transition">Início</a></li>
        <li aria-hidden="true">/</li>
        <li><a href="/#servicos" class="hover:text-gold-500 transition">Serviços</a></li>
        <li aria-hidden="true">/</li>
        <li class="text-prime-900 font-semibold" aria-current="page">{s['title']}</li>
      </ol>
    </div>
  </nav>

  <section class="hero-bg pt-16 pb-32">
    <div class="hero-content max-w-4xl mx-auto px-6 lg:px-8 text-center">
      <span class="inline-block border border-gold-400/30 text-gold-400 font-bold tracking-widest uppercase text-xs px-5 py-2 rounded-full mb-6">Serviço</span>
      <div class="w-20 h-20 rounded-full border border-gold-400/30 flex items-center justify-center mx-auto mb-8 text-gold-400 text-3xl" aria-hidden="true">
        <i class="{s['icon_lib']} {s['icon']}"></i>
      </div>
      <h1 class="font-serif text-4xl sm:text-5xl lg:text-6xl text-white mb-6 leading-tight uppercase">{s['title']}</h1>
      <p class="text-white/70 text-lg leading-relaxed max-w-2xl mx-auto">{s['tagline']}</p>
    </div>
  </section>
'''


def main():
    for svc in SERVICES:
        slug = svc['slug']
        dest_dir = os.path.join(ROOT, 'servicos', slug)
        assets_dir = os.path.join(dest_dir, 'assets')
        os.makedirs(assets_dir, exist_ok=True)

        img_name = os.path.basename(svc['image_src'])
        shutil.copy2(os.path.join(ROOT, svc['image_src']), os.path.join(assets_dir, img_name))

        benefits_html = ''.join(
            f'<article class="bg-prime-50 p-8 border border-prime-100"><h3 class="font-serif text-lg text-prime-900 mb-3 uppercase">{b[0]}</h3><p class="text-prime-600 font-light text-sm leading-relaxed">{b[1]}</p></article>'
            for b in svc['benefits']
        )
        includes_html = ''.join(
            f'<li class="flex items-start gap-3"><i class="fas fa-check text-gold-400 mt-1 text-xs" aria-hidden="true"></i><span class="text-prime-600 font-light text-sm">{item}</span></li>'
            for item in svc['includes']
        )
        others_html = ''.join(
            f'<li><a href="/servicos/{s["slug"]}/" class="text-prime-600 hover:text-gold-500 transition text-sm font-light">{s["title"]}</a></li>'
            for s in SERVICES if s['slug'] != slug
        )

        schema = json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "name": svc['title'],
            "description": svc['summary'],
            "provider": {"@type": "Organization", "name": "Conceito Prime", "url": "https://conceitop.com.br"},
            "areaServed": "Curitiba, PR",
            "url": f"https://conceitop.com.br/servicos/{slug}/"
        }, ensure_ascii=False)

        body = f'''
  <section class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-16 items-center">
        <div>
          <div class="w-12 h-[1px] bg-gold-400 mb-8" aria-hidden="true"></div>
          <h2 class="font-serif text-3xl sm:text-4xl text-prime-900 mb-6 uppercase leading-tight">Sobre o <span class="text-gold-400">serviço</span></h2>
          <p class="text-prime-600 font-light text-[15px] leading-[1.8] mb-6">{svc['intro']}</p>
          <p class="text-prime-600 font-light text-[15px] leading-[1.8]">{svc['summary']}</p>
        </div>
        <figure class="m-0">
          <img src="assets/{img_name}" alt="{svc['image_alt']}" width="800" height="800" class="w-full object-cover aspect-[4/3] border border-prime-100" loading="lazy" decoding="async">
        </figure>
      </div>
    </div>
  </section>

  <section class="py-24 bg-prime-50" aria-labelledby="incluso-{slug}">
    <div class="max-w-4xl mx-auto px-6 lg:px-8">
      <h2 id="incluso-{slug}" class="font-serif text-3xl text-prime-900 mb-10 uppercase text-center">O que está <span class="text-gold-400">incluso</span></h2>
      <ul class="grid sm:grid-cols-2 gap-4">{includes_html}</ul>
    </div>
  </section>

  <section class="py-24 bg-white" aria-labelledby="beneficios-{slug}">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <h2 id="beneficios-{slug}" class="font-serif text-3xl text-prime-900 mb-12 uppercase text-center">Principais <span class="text-gold-400">benefícios</span></h2>
      <div class="grid sm:grid-cols-2 gap-6">{benefits_html}</div>
    </div>
  </section>

  <section class="py-16 bg-prime-50 border-t border-prime-100" aria-labelledby="outros-{slug}">
    <div class="max-w-4xl mx-auto px-6 lg:px-8 text-center">
      <h2 id="outros-{slug}" class="font-serif text-xl text-prime-900 mb-6 uppercase">Outros serviços</h2>
      <ul class="flex flex-wrap justify-center gap-x-6 gap-y-3">{others_html}</ul>
    </div>
  </section>
'''

        html = render_head(svc, schema) + body + render_footer(svc['title'])
        with open(os.path.join(dest_dir, 'index.html'), 'w') as f:
            f.write(html)
        print(f'Created servicos/{slug}/')


if __name__ == '__main__':
    main()
