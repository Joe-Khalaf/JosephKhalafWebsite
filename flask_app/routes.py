from datetime import datetime
from flask import current_app as app, abort, render_template, redirect, url_for


PROFESSIONAL_PROJECTS = [
    {
        "slug": "tankvision", "number": "01", "name": "TankVision", "category": "IoT · Fuel Operations", "color": "lime", "art": "telemetry",
        "logo": "main/images/TankVisionLogo_NoBackground.png",
        "short": "Remote tank intelligence for smarter fuel dispatch and compliance.",
        "headline": "A connected operations platform that turns fuel-tank telemetry into timely, actionable decisions.",
        "focus": "IoT platform", "problem_title": "Making every tank visible from anywhere.",
        "description": "TankVision connects on-site agents—currently Raspberry Pi devices, with a custom ESP32 PCB planned—to automatic tank gauges across a network of gas stations. It gives the business one place to understand fuel levels, compliance, trends, alerts, and reports so dispatch decisions can happen with better information and less guesswork.",
        "technical_summary": "I work across TankVision's web, API, data, and edge-device layers. A React and TypeScript frontend provides responsive dashboards and visualizations, while a Python FastAPI backend handles authenticated APIs, device ingestion, reporting, and background processing. PostgreSQL provides persistent storage and Redis supports device-command messaging and queued work.",
        "capabilities": ["Live fuel inventory across distributed sites", "Historical trends, forecasting, and delivery planning", "Compliance records, alerts, and system-health visibility", "PDF and CSV operational reporting", "Remote device administration and firmware management", "Offline-resilient telemetry collection"],
        "architecture": [
            {"title": "Web application", "text": "React, TypeScript, Vite, Tailwind CSS, and Recharts power responsive operational dashboards and data visualization."},
            {"title": "API and data", "text": "FastAPI, Pydantic, and SQLAlchemy provide authenticated REST APIs over PostgreSQL, with Redis supporting commands and queued work."},
            {"title": "Edge agents", "text": "A resilient Python agent for Linux and Raspberry Pi communicates with ATGs over serial protocols, buffers data locally in SQLite, and synchronizes after connectivity returns."},
            {"title": "Embedded platform", "text": "A newer C++ agent targets custom ESP32-S3 hardware using PlatformIO, Ethernet or Wi-Fi, flash-based offline storage, watchdog recovery, a local configuration portal, and OTA updates."},
            {"title": "Security and operations", "text": "Role-based OIDC authentication, encrypted device communication, Docker containers, automated tests, administrative tooling, and PDF/CSV reporting support production use."}
        ],
        "technology_groups": [
            {"label": "Frontend", "items": "React · TypeScript · Vite · Tailwind CSS · Recharts"},
            {"label": "Backend", "items": "Python · FastAPI · Pydantic · SQLAlchemy"},
            {"label": "Data", "items": "PostgreSQL · Redis · SQLite"},
            {"label": "Embedded", "items": "ESP32-S3 · C++ · PlatformIO · Serial integration"},
            {"label": "Platform", "items": "Docker · Caddy · Nginx · pytest · OIDC/JWT"}
        ],
        "features": [
            {"title": "Connected infrastructure", "text": "On-site agents communicate with ATGs and securely surface station data to a central web platform."},
            {"title": "Operational awareness", "text": "Live levels, alerts, compliance signals, analytics, and reports make exceptions easy to spot."},
            {"title": "Better dispatch decisions", "text": "The product helps teams determine when stations need fuel while creating value beyond dispatch."}
        ],
        "tags": ["IoT architecture", "Edge devices", "Real-time data", "Alerts", "Analytics", "Product design"]
    },
    {
        "slug": "chillbox-toolbox", "number": "02", "name": "Chillbox Toolbox", "category": "Data Product · Retail Intelligence", "color": "blue", "art": "analytics",
        "logo": "main/images/ChillboxToolboxLogoNoBackground.png",
        "short": "Real-time retail intelligence shaped around how the business actually works.",
        "headline": "A practical intelligence layer for transaction data across convenience-store operations.",
        "focus": "Analytics platform", "problem_title": "Turning transaction logs into a shared operating picture.",
        "description": "Chillbox Toolbox transforms Verifone Commander transaction logs into focused, accessible views of the business. Instead of digging through systems that were not designed for the team's questions, leaders can monitor loyalty, loss prevention, sales, cashier performance, reporting, live fuel prices, and comparisons across sites in near real time.",
        "technical_summary": "I built Chillbox Toolbox as a production-oriented analytics platform with a React 19 and TypeScript single-page application, a Python and Flask REST API, and PostgreSQL. It ingests and normalizes data from Verifone point-of-sale systems, TankVision, BPSC fuel records, and Google Sheets into a unified relational model designed around the company's operational questions.",
        "capabilities": ["Company-wide and store-level sales performance", "Fuel pricing, margins, gallons, and TankVision reconciliation", "Loyalty participation, customer lift, and cashier enrollment", "Transaction timelines with receipts and journal events", "Loss-prevention scoring and direct investigative drill-downs", "Store, cashier, product, department, brand, and vendor search", "CSV and PDF exports plus scheduled email reports", "Granular store, report, margin, export, and camera permissions"],
        "architecture": [
            {"title": "Investigative interface", "text": "Reusable React components support KPI dashboards, charts, date ranges, drill-downs, URL-backed filters, large paginated datasets, and responsive mobile navigation."},
            {"title": "Domain-driven API", "text": "Flask routers and services separate dashboards, stores, products, transactions, reports, loyalty, fuel pricing, loss prevention, alerts, cameras, and administration."},
            {"title": "Analytics at scale", "text": "Incremental daily rollups keep store, cashier, product, brand, loyalty, promotion, fuel-price, and competition analytics responsive as transaction volume grows."},
            {"title": "Continuous ingestion", "text": "An independent polling service retrieves Verifone activity, processes BPSC data, updates fuel pricing and margins, rebuilds affected rollups, reconciles alerts, and dispatches scheduled reports."},
            {"title": "Layered security", "text": "Microsoft Entra ID, validated JWTs, application roles, and database-managed authorization enforce store- and feature-level permissions. Short-lived camera tokens avoid exposing protected endpoints or credentials."},
            {"title": "Production operations", "text": "Docker Compose separates PostgreSQL, the Gunicorn API, and poller services, supported by health checks, locking, structured logs, Prometheus metrics, Grafana observability, and pytest coverage."}
        ],
        "technology_groups": [
            {"label": "Frontend", "items": "React 19 · TypeScript · React Router · Recharts · MSAL"},
            {"label": "Backend", "items": "Python · Flask · Gunicorn · SQLAlchemy 2"},
            {"label": "Data and ETL", "items": "PostgreSQL · Incremental rollups · Verifone · BPSC · TankVision"},
            {"label": "Security", "items": "Microsoft Entra ID · OAuth · RS256 JWT · Role-based authorization"},
            {"label": "Operations", "items": "Docker Compose · Prometheus · Grafana · Loki · pytest"}
        ],
        "features": [
            {"title": "Business-specific analytics", "text": "Views are built around the questions operators actually ask, not generic dashboards."},
            {"title": "Cross-site visibility", "text": "Teams can compare locations, prices, performance, and unusual activity in one workflow."},
            {"title": "Faster signals", "text": "Near-real-time processing makes important trends and exceptions useful while action can still be taken."}
        ],
        "tags": ["Data pipelines", "Full-stack", "Retail systems", "Dashboards", "Loss prevention", "UX"]
    },
    {
        "slug": "airware", "number": "03", "name": "AirWare", "category": "IoT · Field Operations", "color": "orange", "art": "device",
        "logo": "main/images/ChillboxAirWareLogoFinal.png",
        "short": "Equipment telemetry turned into clear priorities for field teams.",
        "headline": "A responsive operations platform for monitoring equipment health, collection needs, and field activity across multiple locations.",
        "focus": "Equipment operations", "problem_title": "Giving field teams one clear view of distributed equipment.",
        "description": "AirWare turns incoming air and vacuum machine data into an actionable view of equipment health, collection needs, and recent activity. Employees can identify locations requiring attention, record completed collections from a mobile device, receive operational alerts, and review performance trends from one centralized application.",
        "technical_summary": "I designed and developed AirWare as a full-stack, cloud-deployed telemetry application using React, TypeScript, Python, and Flask. It normalizes external equipment feeds, combines them with field activity recorded by employees, and exposes the resulting operational state through authenticated REST APIs.",
        "capabilities": ["Live equipment status and stale-data monitoring", "Mobile collection workflows with geolocation assistance", "Automated operational alerts and lifecycle tracking", "Usage, collection, revenue, and performance analytics", "Projected service and collection needs", "Role-restricted administration and Microsoft single sign-on"],
        "architecture": [
            {"title": "Responsive field experience", "text": "React, TypeScript, and Material UI provide desktop dashboards and mobile collection workflows, with geolocation assistance reducing manual entry in the field."},
            {"title": "Telemetry ingestion", "text": "The Flask backend ingests and parses external machine feeds, normalizes their data, and combines it with internally recorded field activity."},
            {"title": "Operational intelligence", "text": "Equipment-state calculations, scheduled snapshots, Recharts analytics, and projections surface abnormal conditions and locations likely to need service."},
            {"title": "Alerts and notifications", "text": "Automated processing creates, updates, and resolves operational alerts while notification workflows keep the appropriate employees informed."},
            {"title": "Secure access", "text": "Microsoft Entra ID token validation and role-based controls protect administration, while validated APIs and restricted cross-origin access guard external data flows."},
            {"title": "Delivery and reliability", "text": "SQLAlchemy persistence, Docker containers, Azure-hosted services, GitHub Actions CI/CD, and backend tests support reliable production operation."}
        ],
        "technology_groups": [
            {"label": "Frontend", "items": "React · TypeScript · Material UI · Recharts"},
            {"label": "Backend", "items": "Python · Flask · SQLAlchemy · REST APIs"},
            {"label": "Identity", "items": "Microsoft Entra ID · Token validation · Role-based access"},
            {"label": "Platform", "items": "Docker · Azure · GitHub Actions · Automated testing"}
        ],
        "features": [
            {"title": "Clear priorities", "text": "A centralized status view highlights stale data, abnormal conditions, and locations needing attention."},
            {"title": "Field-friendly collections", "text": "Employees can record completed collections from a phone with geolocation assistance and less manual entry."},
            {"title": "Performance visibility", "text": "Usage, collections, revenue, and trends make machine performance measurable and service needs easier to anticipate."}
        ],
        "tags": ["React", "TypeScript", "Python", "Flask", "Telemetry", "Azure", "Field operations"]
    },
    {
        "slug": "bazco-autoaccounting", "number": "04", "name": "Bazco AutoAccounting", "category": "Automation · Accounting", "color": "violet", "art": "sheets",
        "logo": "main/images/cropped-bazco-logo.webp",
        "short": "Validated financial workbooks without repetitive spreadsheet assembly.",
        "headline": "A secure internal application that turns accounting exports into standardized, review-ready workbooks.",
        "focus": "Accounting automation", "problem_title": "Making recurring accounting work repeatable and controlled.",
        "description": "Bazco AutoAccounting replaces manual report combining, value transfer, and import formatting with straightforward upload workflows. Employees provide their CSV, Excel, or ZIP source files and receive completed workbooks ready for review. It currently supports monthly sales-tax reporting, consolidated operational worksheets, and weekly payment-processing workflows.",
        "technical_summary": "I designed and built Bazco AutoAccounting as a full-stack application that transforms CSV, Excel, and ZIP-based exports into validated financial workbooks. A responsive React and TypeScript interface guides employees through each workflow, while independent Python Azure Functions normalize source data, reconcile records, perform accounting calculations, and generate formatted Excel deliverables.",
        "capabilities": ["Monthly sales-tax reporting", "Consolidated operational worksheets", "Weekly payment-processing workflows", "CSV, XLS, XLSX, and ZIP ingestion", "Cross-file reconciliation and normalization", "Automatic, standardized workbook downloads"],
        "architecture": [
            {"title": "Accessible upload workflows", "text": "A React, TypeScript, and Vite single-page application provides drag-and-drop inputs, workflow-specific fields, processing feedback, and automatic downloads."},
            {"title": "Serverless processing", "text": "Independent Python Azure Functions isolate each accounting workflow and scale processing without requiring a continuously running application server."},
            {"title": "Validation pipeline", "text": "Schema, filename, date, mapping, duplicate, and value checks stop incomplete or unsupported inputs before an accounting output is produced."},
            {"title": "Data reconciliation", "text": "pandas-based processing parses varied source formats, normalizes values, matches records across files, and applies the required accounting calculations."},
            {"title": "Excel generation", "text": "openpyxl creates familiar workbooks programmatically with formulas, formatting, totals, and print-ready layouts."},
            {"title": "Secure internal use", "text": "Microsoft authentication, role-based access, file-size limits, safe ZIP handling, spreadsheet-injection protection, and security headers protect the workflow."}
        ],
        "technology_groups": [
            {"label": "Frontend", "items": "React · TypeScript · Vite · Drag-and-drop file workflows"},
            {"label": "Processing", "items": "Python · pandas · openpyxl · Data validation"},
            {"label": "Platform", "items": "Azure Functions · Serverless endpoints · Microsoft authentication"},
            {"label": "File support", "items": "CSV · XLS · XLSX · ZIP · Generated Excel workbooks"}
        ],
        "features": [
            {"title": "Familiar inputs", "text": "Employees upload the reports they already receive instead of re-entering their contents or learning a complicated new process."},
            {"title": "Controlled processing", "text": "Validation and repeatable business rules catch incomplete data and apply calculations consistently."},
            {"title": "Familiar outputs", "text": "The result remains a formatted, reviewable Excel workbook that fits the accounting team's existing process."}
        ],
        "tags": ["React", "TypeScript", "Python", "Azure Functions", "pandas", "openpyxl", "Data validation"]
    },
    {
        "slug": "storage-lot-manager", "number": "05", "name": "Storage Lot Manager", "category": "Internal Tool · Property Operations", "color": "pink", "art": "map",
        "logo": "main/images/ChillboxLogo.jpg",
        "context": "Internal operations platform",
        "short": "A physical storage facility transformed into a centralized digital workflow.",
        "headline": "A full-stack operations platform for managing spaces, customers, rentals, payments, alerts, and historical records.",
        "focus": "Storage operations", "problem_title": "Turning a physical lot into an interactive workspace.",
        "description": "I designed and built a web-based storage management platform that transforms a facility's real-world layout into an interactive digital workspace. Employees can quickly understand space and account status, select a space to manage its customer and rental information, record payments, coordinate follow-up activity, and generate operational reports without relying on fragmented paper or spreadsheet processes.",
        "technical_summary": "I built the platform as a responsive JavaScript, HTML, and CSS application with Vite and a modular Python Flask REST API. PostgreSQL provides production persistence, with SQLite supporting local development. The relational model preserves connections between customers, rentals, spaces, payments, and alerts so closed rentals retain complete historical records.",
        "capabilities": ["Interactive, color-coded facility map", "Customer and multi-space rental management", "Payment recording and account-status calculations", "Automated upcoming and overdue account detection", "Configurable reminders and internal notifications", "Follow-up notes for account alerts", "Current-customer, payment-history, and overdue reporting", "Read-only, operational, and administrator access levels"],
        "architecture": [
            {"title": "Interactive facility map", "text": "A responsive, color-coded interface mirrors the physical facility and makes space status and related workflows understandable at a glance."},
            {"title": "Modular operations API", "text": "Feature-specific Flask API modules separate spaces, customers, rentals, payments, alerts, reporting, and administration."},
            {"title": "Historical data model", "text": "Relationships between customers, spaces, rentals, payments, and alerts preserve operational history even after a rental closes."},
            {"title": "Payment awareness", "text": "Recording, allocation, and account-status calculations support automated detection of upcoming and overdue accounts without exposing internal business rules."},
            {"title": "Enterprise access", "text": "Microsoft Entra ID validates JWT access tokens, while role-based authorization separates read-only, operational, and administrative capabilities."},
            {"title": "Deployment and verification", "text": "Docker packages the Flask and PostgreSQL application, and automated authorization tests verify access boundaries across employee roles."}
        ],
        "technology_groups": [
            {"label": "Frontend", "items": "JavaScript · HTML · CSS · Vite · Responsive UI"},
            {"label": "Backend", "items": "Python · Flask · Modular REST APIs"},
            {"label": "Data", "items": "PostgreSQL · SQLite · Relational history"},
            {"label": "Security", "items": "Microsoft Entra ID · JWT validation · Role-based authorization"},
            {"label": "Platform", "items": "Docker · Automated authorization testing"}
        ],
        "features": [
            {"title": "Visual daily operations", "text": "The interface mirrors the physical facility so employees can understand availability and account status at a glance."},
            {"title": "Connected records", "text": "Customers, multi-space rentals, payments, alerts, and follow-up notes remain connected through one workflow."},
            {"title": "Reliable follow-through", "text": "Automated account detection, configurable reminders, and historical reports keep important work visible."}
        ],
        "tags": ["JavaScript", "Python", "Flask", "PostgreSQL", "Microsoft Entra ID", "Docker", "REST APIs"]
    },
    {
        "slug": "business-automations", "number": "06", "name": "Business Automations", "category": "Automation · Developer Productivity", "color": "yellow", "art": "workflow",
        "logos": ["main/images/cropped-bazco-logo.webp", "main/images/ChillboxLogo.jpg"],
        "short": "Targeted integrations that keep business-critical data and tasks moving.",
        "headline": "A portfolio of reliable workflows connecting financial, retail, loyalty, inventory, logistics, website, and communication systems.",
        "focus": "Systems integration", "problem_title": "Treating repeated manual work as an integration opportunity.",
        "description": "I develop targeted automations that replace repetitive administrative processes with reliable, traceable workflows. Together, these projects reduce manual entry, standardize reporting, coordinate time-sensitive work, and move operational data consistently between the systems used across the business.",
        "technical_summary": "The automation portfolio combines Python services, REST API integrations, OAuth, SFTP transfers, scheduled jobs, Microsoft Power Automate, structured file transformation, notifications, stateful deduplication, validation, retry handling, and cross-system synchronization. Each workflow is intentionally narrow, but designed with the reliability expected of a business-critical integration.",
        "capabilities": ["Financial and accounting data movement", "Retail sales and fuel reporting", "Loyalty-platform file synchronization", "Inventory and logistics integration", "Customer-facing price updates", "Structured requests, reminders, and notifications"],
        "automations": [
            {"name": "Zoho Invoice Automation", "practical": "Retrieves new invoices and converts line items into standardized import files, reducing repetitive financial entry.", "technical": "A Python integration uses Zoho REST APIs and OAuth, with pagination, concurrent retrieval, rate limiting, retries, stateful deduplication, logging, and Teams notifications."},
            {"name": "BPSC Daily Sales Data + Product Breakdown", "practical": "Collects daily sales across retail locations and produces standardized imports plus detailed fuel-sales reports for reconciliation.", "technical": "A continuously running Python service monitors closing activity, retrieves API data, applies configurable mappings, combines inventory readings, validates CSV outputs, tracks state in SQLite, and distributes reports."},
            {"name": "PDI → Paytronix Cashier File", "practical": "Converts cashier data from PDI into Paytronix's required format without manual editing or store-assignment errors.", "technical": "A scheduled Python pipeline retrieves TSV data through SFTP, validates and remaps store identifiers, preserves the required structure, and delivers output to a separate secure destination."},
            {"name": "Tank Charts + Readings to Gravitate", "practical": "Keeps tank configuration and current inventory readings synchronized with Gravitate.", "technical": "Python integrations normalize tank metadata, capacity charts, and live readings from external APIs, with SQLite deduplication, batch processing, timestamp normalization, authentication, and partial-failure handling."},
            {"name": "Live Prices to the Chillbox Website", "practical": "Keeps customer-facing fuel prices on the company website current without repeated manual updates.", "technical": "A scheduled integration normalizes price events across locations. FastAPI, React, Vite, SQLite, and Docker support incremental synchronization, price history, lifecycle deduplication, retention, and missed-window recovery."},
            {"name": "Store Supply Requests", "practical": "Gives stores a consistent request process and routes submissions to the appropriate employees for follow-up.", "technical": "A Power Automate workflow captures structured data and applies routing and notification rules across Microsoft 365."},
            {"name": "Promotion Change Reminders", "practical": "Reminds employees when promotional materials need to be installed, changed, or removed.", "technical": "A scheduled Power Automate workflow evaluates promotion dates and sends targeted notifications using configurable timing and recipient rules."},
            {"name": "Fuel Surcharge Automation", "practical": "Calculates the weekly fuel surcharge, communicates changes, and updates the logistics platform for the next billing period.", "technical": "A Python service retrieves EIA diesel pricing, applies a configurable rate table, determines the effective period, and updates a logistics API. Idempotent state prevents duplicates while Power Automate coordinates scheduling and notifications."},
            {"name": "Rebate-Cycle Billing Reminders", "practical": "Tracks recurring rebate milestones and reminds employees when billing or reconciliation work is approaching.", "technical": "A date-driven Power Automate workflow centralizes recurring timing and notification logic in Microsoft 365."}
        ],
        "architecture": [
            {"title": "API integrations", "text": "Authenticated REST integrations move financial, retail, pricing, tank, and logistics data between specialized platforms."},
            {"title": "File pipelines", "text": "CSV and TSV transformation plus SFTP transfers validate, reshape, and deliver structured data for downstream systems."},
            {"title": "Reliable scheduling", "text": "Long-running services, scheduled jobs, and Power Automate flows coordinate polling, calculations, reminders, and delivery."},
            {"title": "Safe processing", "text": "Validation, retries, rate limiting, stateful deduplication, logging, and partial-failure handling prevent silent or duplicate work."},
            {"title": "Operational communication", "text": "Email, Teams, and Microsoft 365 notifications make results, failures, requests, and approaching deadlines visible."}
        ],
        "technology_groups": [
            {"label": "Development", "items": "Python · FastAPI · React · Vite"},
            {"label": "Integration", "items": "REST APIs · OAuth · SFTP · CSV/TSV transformation"},
            {"label": "Automation", "items": "Power Automate · Scheduled services · GitHub Actions"},
            {"label": "Reliability", "items": "SQLite state · Validation · Retries · Deduplication · Logging"},
            {"label": "Communication", "items": "Microsoft Teams · Email · Microsoft 365"}
        ],
        "features": [
            {"title": "Connect existing systems", "text": "Focused integrations bridge platforms without forcing teams to replace the tools that already support their work."},
            {"title": "Build reliability in", "text": "Validation, state tracking, retries, and failure notifications make unattended processes safe to depend on."},
            {"title": "Keep people informed", "text": "Automated reports, reminders, and alerts surface results and exceptions without adding coordination overhead."}
        ],
        "tags": ["Python", "REST APIs", "SFTP", "Power Automate", "OAuth", "SQLite", "Docker"]
    },
    {
        "slug": "gm-waste-management", "number": "07", "name": "GM Waste Management", "category": "Industry Capstone · Sustainability", "color": "blue", "art": "sustainability",
        "logo": "main/images/GM Logo.png",
        "context": "Michigan State University · General Motors", "role": "Team Lead & Software Engineer",
        "short": "Waste-data validation, anomaly detection, and forecasting for manufacturing plants.",
        "headline": "A full-stack dashboard designed with General Motors to help manufacturing facilities report accurate waste data and track progress toward sustainability goals.",
        "focus": "Data and machine learning", "problem_title": "Making manufacturing waste data easier to trust and act on.",
        "description": "For my Michigan State University computer science capstone, our team worked with General Motors on a Global Waste Management System for its manufacturing operations. The application replaces error-prone spreadsheet entry with a structured web workflow that validates monthly waste records, surfaces anomalies, preserves review notes, visualizes historical trends, and helps managers understand projected waste volumes.",
        "technical_summary": "The team developed a React frontend, Python Flask backend, and MySQL data layer packaged with Docker. Python analytics process historical facility records for anomaly detection and future-trend visualization. My documented contributions included user authentication, data encryption, the future-prediction algorithm, graph and pie-chart modals, and anomaly detection for missing shipments.",
        "gallery": [
            {"image": "main/images/gm-capstone/image7.png", "title": "Anomaly dashboard", "text": "Flagged records are organized by status with the reason each shipment requires review."},
            {"image": "main/images/gm-capstone/image9.png", "title": "Future predictions", "text": "Historical waste readings and projected trends are presented in explorable chart modals."},
            {"image": "main/images/gm-capstone/image10.png", "title": "Structured data entry", "text": "A guided ticket workflow replaces direct entry into a large monthly spreadsheet."}
        ],
        "capabilities": ["Structured monthly waste-data entry", "Real-time anomaly checks before submission", "Reviewable anomaly status and notes", "Historical data filtering and correction", "Waste trend and sustainability visualizations", "Future waste-volume forecasting", "Standardized report generation", "Facility-aware access and data views"],
        "architecture": [
            {"title": "Operational dashboard", "text": "A React interface supports anomaly review, structured data entry, historical records, filtering, editing, and visual reporting."},
            {"title": "Analytics API", "text": "A Python Flask backend processes requests, validates records, runs statistical analysis, and serves facility-specific waste information."},
            {"title": "Anomaly detection", "text": "Statistical and machine-learning techniques flag unusual quantities, missing shipments, and likely entry errors before inaccurate data moves forward."},
            {"title": "Forecasting", "text": "Historical data and production expectations support trend analysis and future waste-volume estimates for sustainability planning."},
            {"title": "Data and deployment", "text": "MySQL stores structured reports, anomalies, and historical trends, while Docker provides a consistent application environment."},
            {"title": "My contribution", "text": "I implemented authentication, encryption, forecasting, visualization modals, and missing-shipment anomaly detection, while helping lead team workflow and sponsor communication."}
        ],
        "technology_groups": [
            {"label": "Frontend", "items": "React · JavaScript · HTML · CSS · Data visualization"},
            {"label": "Backend", "items": "Python · Flask · REST APIs"},
            {"label": "Data", "items": "MySQL · pandas · Historical waste records"},
            {"label": "Analytics", "items": "scikit-learn · PyOD · Statistical anomaly detection · Forecasting"},
            {"label": "Platform", "items": "Docker · Authentication · Encryption"}
        ],
        "features": [
            {"title": "More accurate reporting", "text": "Structured inputs, standardization, and anomaly checks reduce preventable errors in monthly facility data."},
            {"title": "Reviewable exceptions", "text": "Managers can investigate flagged records, document decisions, correct data, or acknowledge valid anomalies."},
            {"title": "Progress over time", "text": "Historical views and forecasting help teams understand waste trends in the context of long-term sustainability goals."}
        ],
        "tags": ["React", "Python", "Flask", "MySQL", "Machine learning", "Docker", "Data visualization"]
    },
    {
        "slug": "little-caesars-observability", "number": "08", "name": "Fundraising Observability", "category": "Software Engineering Internship · Reliability", "color": "orange", "art": "observability",
        "context": "Little Caesars", "role": "Backend Software Engineering Intern", "logo": "main/images/Little-Caesars-Symbol.png",
        "short": "Actionable telemetry and service-level monitoring for a customer-facing fundraising platform.",
        "headline": "Backend observability designed to help engineers catch reliability and performance problems before they disrupt fundraising customers.",
        "focus": "Observability and reliability", "problem_title": "Turning application behavior into an early-warning system.",
        "description": "During my Little Caesars internship, my primary project was improving visibility into the backend of the fundraising website. I added meaningful logs and metrics that helped the team understand runtime, availability, request performance, errors, and unusual traffic. Dashboards and alerts made changes in system behavior easier to recognize, reducing the risk of extended software issues and helping protect a dependable customer experience.",
        "technical_summary": "I made targeted changes throughout an established C# backend to add useful application logs and metrics, sent those signals into Azure, and wrote KQL queries to turn raw events into operational measures. I then used Nobl9 and Grafana to define and visualize service-level objectives, performance indicators, and alerts for slow requests, errors, unusually high usage, and availability concerns. Just as importantly, the internship taught me how to contribute within a large engineering organization through Scrum ceremonies, scoped tickets, code review, unit testing, CI/CD work, and collaboration with experienced engineers.",
        "capabilities": ["Runtime and request-duration visibility", "Availability and uptime monitoring", "Slow-request and error-rate alerts", "Unusual traffic and usage detection", "Service-level objectives and indicators", "Grafana operational dashboards", "KQL-based telemetry analysis", "Earlier awareness of customer-impacting regressions"],
        "architecture": [
            {"title": "Application instrumentation", "text": "Purposeful backend logs and metrics expose request timing, failures, traffic patterns, and other signals tied to platform health."},
            {"title": "Telemetry analysis", "text": "Azure receives application signals, while KQL queries transform raw events into useful measurements and investigative views."},
            {"title": "Service-level monitoring", "text": "Nobl9 SLOs connect reliability targets to measured behavior, making availability and performance easier to evaluate over time."},
            {"title": "Dashboards and alerts", "text": "Grafana visualizations and targeted alerts highlight slow requests, rising errors, unusual load, and other meaningful changes."},
            {"title": "Engineering quality", "text": "Unit tests, code review, and CI/CD contributions improved confidence when changing a mature, customer-facing system."},
            {"title": "Team development", "text": "Working in Scrum on a large team taught me to navigate an existing codebase, communicate progress, respond to review feedback, and ship within established standards."}
        ],
        "technology_groups": [
            {"label": "Backend", "items": "C# · Application instrumentation · Structured logging"},
            {"label": "Observability", "items": "Grafana · Nobl9 · Service-level objectives · Alerts"},
            {"label": "Cloud and data", "items": "Microsoft Azure · KQL · Application telemetry"},
            {"label": "Quality", "items": "Unit testing · Code review · Regression prevention"},
            {"label": "Delivery", "items": "Azure DevOps · YAML · CI/CD pipelines"},
            {"label": "Team practices", "items": "Scrum · Sprint planning · Collaborative development"}
        ],
        "features": [
            {"title": "Earlier detection", "text": "Alerts bring emerging performance, traffic, and error patterns to the team before they become prolonged customer issues."},
            {"title": "Shared visibility", "text": "Dashboards give engineers a common view of the fundraising platform's runtime behavior and service health."},
            {"title": "Measurable reliability", "text": "SLOs turn broad expectations like speed and uptime into concrete signals the team can track and improve."}
        ],
        "tags": ["Azure", "KQL", "Grafana", "Nobl9", "SLOs", "Testing", "CI/CD"]
    }
]

ARCHIVE_PROJECTS = [
    {"name": "Communicate.AI", "type": "Hackathon · AR / AI", "description": "Live translated subtitles overlaid beneath a speaker.", "url": "/mhacks16", "image": "main/images/MHacks Logo.png"},
    {"name": "Connect-4 AI", "type": "Machine Learning · 1st Place", "description": "Multiple learning strategies trained and compared on Connect-4.", "url": "/connect4", "image": "main/images/connect4.jpg"},
    {"name": "Robofest", "type": "Robotics · 3rd Worldwide", "description": "Autonomous robots designed and programmed for competition.", "url": "/robofest", "image": "main/images/robofest.jpg"},
    {"name": "Trello-like App", "type": "Full-stack", "description": "A collaborative task-management experience built from scratch.", "url": "/trello", "image": "main/images/trello.png"},
    {"name": "CanadianExperience", "type": "C++ · Animation", "description": "A desktop animation system with interactive scene tools.", "url": "/canadianexperience", "image": "main/images/canadianexperiencepic.png"},
    {"name": "Wordle Helper", "type": "Algorithm", "description": "A utility that narrows possible solutions from known clues.", "url": "/wordlehelp", "image": "main/images/WordleHelpPhoto.png"},
    {"name": "Halloween Sudoku", "type": "Game Development", "description": "A themed, playable Sudoku game experience.", "url": "/sudoku", "image": "main/images/halloween sudoku.png"},
    {"name": "Interactive Piano", "type": "Creative Coding", "description": "A browser piano with a hidden interactive surprise.", "url": "/piano", "image": "main/images/piano.jpeg"}
]


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


@app.route('/')
def home():
    return render_template('home.html', featured_projects=PROFESSIONAL_PROJECTS[:3])


@app.route('/home')
def home_legacy():
    return redirect(url_for('home'), code=301)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', professional_projects=PROFESSIONAL_PROJECTS, archive_projects=ARCHIVE_PROJECTS)


@app.route('/projects/<slug>')
def professional_project(slug):
    project = next((item for item in PROFESSIONAL_PROJECTS if item['slug'] == slug), None)
    if project is None:
        abort(404)
    index = PROFESSIONAL_PROJECTS.index(project)
    next_project = PROFESSIONAL_PROJECTS[(index + 1) % len(PROFESSIONAL_PROJECTS)]
    return render_template('professional_project.html', project=project, next_project=next_project)


@app.route('/resume')
def resume(): return render_template('resume_page.html')


@app.route('/resume/pdf')
def resume_pdf(): return render_template('resume_print.html')

@app.route('/piano')
def piano(): return render_template('piano.html')

@app.route('/mhacks16')
def mhacks16(): return render_template('mhacks16.html')

@app.route('/robofest')
def robofest(): return render_template('robofest.html')

@app.route('/canadianexperience')
def canadianexperience(): return render_template('canadianexperience.html')

@app.route('/wordlehelp')
def wordlehelp(): return render_template('wordlehelp.html')

@app.route('/sudoku')
def sudoku(): return render_template('sudoku.html')

@app.route('/connect4')
def connect4(): return render_template('connect4.html')

@app.route('/trello')
def trello(): return render_template('trello.html')


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, public, max-age=0'
    return response
