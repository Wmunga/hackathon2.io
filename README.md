# HealthTech Follow-Up Reminder System 🏥

A human-centered, AI-powered solution for managing patient follow-ups and appointments, built for the hackathon focusing on joy-driven healthcare solutions.

## 🌟 Project Overview

The Follow-Up Reminder System is designed to bridge the gap between healthcare providers and patients by automating appointment reminders through multiple channels (SMS, WhatsApp, Email) while incorporating AI for smart scheduling and personalized communication.

### Core Features (MVP)

1. **Patient Management**
   - Patient registration and profile management
   - Appointment scheduling and tracking
   - Follow-up history and notes

2. **Smart Reminder System**
   - Multi-channel notifications (SMS, WhatsApp, Email)
   - Automated reminder scheduling
   - Customizable reminder templates

3. **AI-Powered Features**
   - No-show prediction
   - Personalized message generation
   - Smart scheduling recommendations

4. **Healthcare Provider Dashboard**
   - Patient overview
   - Appointment calendar
   - Reminder status tracking
   - Analytics and insights

## 🛠️ Technology Stack (Python-based)

### Backend
- Python 3.9+
- FastAPI (modern, fast web framework)
- SQLite (for development, can upgrade to PostgreSQL)
- SQLAlchemy (database ORM)

### Frontend
- Streamlit (Python-based web framework)
- Plotly for interactive visualizations
- Custom CSS for styling

### AI & Integrations
- OpenAI GPT-4 (via Python SDK)
- Twilio (via Python SDK) for SMS/WhatsApp
- SendGrid (via Python SDK) for email
- Google Calendar API (via Python SDK)

### Development Tools
- Poetry (dependency management)
- Pytest (testing)
- Black (code formatting)
- Flake8 (linting)

## 🎨 UI/UX Highlights

### Joy-Driven Elements
- Interactive data visualizations
- Smooth transitions between pages
- Intuitive form designs
- Clear success/error messages
- Mobile-responsive layouts

### Key Screens
1. **Provider Dashboard**
   - Interactive calendar view
   - Patient management interface
   - Analytics dashboard
   - Quick-action buttons

2. **Patient Portal**
   - Simple appointment booking
   - Reminder preferences
   - Medical history access

3. **Admin Panel**
   - Analytics dashboard
   - System configuration
   - User management

## 🔒 Security & Compliance

- Basic authentication system
- Data encryption
- Role-based access control
- Secure API endpoints
- Data anonymization for testing

## 🚀 Development Timeline

### Day 1 (0-12 hours)
- [ ] Project setup with Poetry
- [ ] Basic database models
- [ ] Authentication system
- [ ] Core API endpoints

### Day 1 (12-24 hours)
- [ ] Streamlit frontend setup
- [ ] Provider dashboard
- [ ] Patient portal
- [ ] Basic reminder system

### Day 2 (0-12 hours)
- [ ] AI integration
- [ ] Notification system
- [ ] Analytics and reporting
- [ ] UI polish

### Day 2 (12-24 hours)
- [ ] Testing and bug fixes
- [ ] Documentation
- [ ] Deployment
- [ ] Presentation preparation

## 📊 Testing Strategy

1. **Unit Tests**
   - API endpoint testing
   - Database model testing
   - AI model testing

2. **Integration Tests**
   - End-to-end workflow testing
   - Third-party service integration
   - Notification system testing

3. **User Acceptance Testing**
   - Provider workflow testing
   - Patient journey testing
   - Edge case handling

## 🎯 Presentation Focus

1. **Demo Flow**
   - Patient registration
   - Appointment scheduling
   - AI-powered reminder generation
   - Multi-channel notification
   - Analytics dashboard

2. **Key Metrics**
   - Reminder effectiveness rate
   - No-show reduction
   - User engagement
   - System reliability

## 🏆 Innovation Highlights

1. **AI Integration**
   - Smart message personalization
   - No-show prediction
   - Optimal timing suggestions

2. **Technical Innovation**
   - Real-time notification system
   - Multi-channel communication
   - Data-driven insights

3. **User Experience**
   - Intuitive interface
   - Interactive visualizations
   - Mobile-first design

## Getting Started

1. Clone the repository
2. Install Python 3.9+ if not already installed
3. Install Poetry (dependency manager):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
4. Install dependencies:
   ```bash
   poetry install
   ```
5. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
6. Run development server:
   ```bash
   poetry run streamlit run src/frontend/app.py
   ```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.