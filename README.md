# College Management System

## Overview

This project is a **College Management System** that allows you to manage colleges, teachers, and students. It includes features such as:

- Adding and displaying **Colleges**
- Adding and displaying **Teachers** and **Students**
- OTP-based authentication for **Teachers** and **Students** using email

## Features

- **Create College**: Register a new college with a unique ID.
- **Add Teacher**: Assign teachers to a college with their email and subject.
- **Add Student**: Add students to a college with their email and branch.
- **Display Teachers & Students**: View details of teachers and students in a specific college.
- **Teacher & Student Login**: OTP-based authentication using Gmail SMTP.

## Technologies Used

- **Python**
- **smtplib** (For sending OTP emails)
- **email.mime** (For structuring emails)
- **random** (For generating OTPs)

## Installation & Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/college-management-system.git
   ```
2. Navigate to the project directory:
   ```sh
   cd college-management-system
   ```
3. Install dependencies (if required):
   ```sh
   pip install smtplib email random
   ```
4. Update the Gmail credentials in the `send_otp()` function:
   ```python
   username = "your-email@gmail.com"
   password = "your-app-password"
   ```
   - Enable **Less Secure Apps** or use an **App Password** for Gmail authentication.

## Usage

Run the script using:

```sh
python college_management.py
```

Follow the menu-driven interface to manage colleges, teachers, and students.

## Example Workflow

1. Create a college.
2. Add teachers and students to the college.
3. Display the list of teachers and students.
4. Perform **OTP-based login** as a teacher or student.

## Contributing

Feel free to submit issues and pull requests to improve the system!


