# Todo website with bale bot

the todo list with send notification from a bale bot

### Features
- Create Todo list
- Send end Time Todos with bale
- Can Create Infinity Todo And Todo list Free!

### Tech Stack
- Backend: Python Django
- Database: SQLite
- Bot: Balethon
- Frontend: HTML, CSS, JavaScript 

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git (optional, for version control)
- [bale](https://bale.ai)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/aboalfazlH/Kharazmi-project
cd Kharazmi-project
   ```

2. **Create a virtual environment**
```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
```bash
pip install -r requirements.txt
   ```

4. **Configure the application**
   - Go to [Botfather]('https://ble.ir/botfather')
   - Create `.env`
   - Copy `.env.example` to `.env`
   - Update the configuration with your settings (bot token, secret key, etc.)

5. **Initialize the database**
```bash
python manage.py migrate
   ```

## Running the Application

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Built with Django
- Special thanks to all contributors