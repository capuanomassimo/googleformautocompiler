# Google Form Autofill for Personal Testing

This project provides a simple Selenium-based script to automatically fill out **your own Google Form**.
It is designed for **functional testing**, QA experiments, or repeated trial submissions on forms that you own or are explicitly authorized to test.

⚠️ It is **not** intended for third-party forms, production environments, or unsolicited submissions.

---

## Features

* Supports common Google Form input types:

  * Radio buttons (single choice)
  * Checkboxes (multiple choice)
  * Dropdown menus
* Randomized selection when no preferred option is found
* Works across multiple form pages (“Next” / “Submit” navigation)
* Configurable loop to repeat submissions
* Small random delays to reduce detection as automated traffic

---

## Demo

![Demo of the script](demo.gif)

---

## Requirements

* Python 3.8+
* [Google Chrome](https://www.google.com/chrome/) installed
* [ChromeDriver](https://chromedriver.chromium.org/) that matches your Chrome version
* Python package `selenium`

Install the dependency with:

```bash
pip install selenium
```

Make sure ChromeDriver is available on your system PATH.

---

## Usage

1. Clone this repository or copy the script into your project folder.
2. Edit the script and set your Google Form URL:

   ```python
   url = "https://docs.google.com/forms/d/e/your-form-id/viewform"
   ```
3. Run the script:

   ```bash
   python main.py
   ```
4. By default, the script will:

   * Fill in answers with random selections
   * Click “Next” until the end of the form
   * Click “Submit” once it reaches the final page
   * Repeat the process up to 400 times (configurable at the bottom of the script)

---

## Notes

The script relies on Google Form’s current HTML structure. If Google updates their frontend, selectors may need adjustments.
Small delays (`time.sleep`) are used to avoid triggering anti-bot checks.
The number of runs (`400` in the example) can be modified by editing the loop at the end of the file.

---

## Disclaimer ⚠️⚠️⚠️⚠️

This project is intended **only for your own Google Form** or forms you have explicit permission to test.
Do **not** use it on third-party forms, surveys, or production systems.
Automated submissions may violate Terms of Service if used improperly.
The script is provided **as is**, without warranty.
You are fully responsible for how you use this code. Use it ethically and responsibly.
