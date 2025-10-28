import flet as ft
from datetime import datetime

def main (page:ft.Page):
    page.title="Homework 5"
    
    email=""
    password=""
    name=""
    address=""
    gender=""
    country=""
    birth=datetime.now
    date_picker=ft.DatePicker(
        first_date=datetime(year=2000, month=10, day=1),
        last_date=datetime(year=2025, month=10, day=31),
    )
    page.overlay.append(date_picker)
    date_text=ft.Text("No date selected")

    def email_value(e):
        nonlocal email
        email=e.control.value

    def password_value(e):
        nonlocal password
        password=e.control.value

    def manage_login(e):
        if email=="" or password=="":
            print("Error: No email or password entered")
            return
        else:
            page.go("/form")

    def name_value(e):
        nonlocal name
        name=e.control.value
    
    def birth_value(e):
        nonlocal birth
        birth=date_picker.value
        if birth:
            date_text.value= f"Selected: {birth.strftime('%Y-%m-%d')}"
        page.update()

    def open_date_picker(e):
        date_picker.open=True
        page.update()

    def address_value(e):
        nonlocal address
        address=e.control.value

    def gender_value(e):
        nonlocal gender
        gender = e.control.value

    def country_value(e):
        nonlocal country
        country=e.control.value

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Home"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ft.TextField(label="Email", on_change=email_value, value=email),
                    ft.TextField(label="Password", 
                                 password=True, 
                                 can_reveal_password=True, 
                                 on_change=password_value, 
                                 value=password),
                    ft.ElevatedButton("Log in", on_click=manage_login),
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=26
            )
        ) 

        if page.route =="/form" and email!="" and password!="":
            page.views.append(
                ft.View(
                    "/form",
                    [
                        ft.AppBar(title=ft.Text("Form"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.TextField(label="Name", on_change=name_value, value=name),
                        ft.Row([
                            ft.ElevatedButton(
                                "Date of birth",
                                icon=ft.Icons.CALENDAR_MONTH,
                                on_click=open_date_picker,
                            ),
                            date_text,
                        ]),
                        ft.Column([
                            ft.Text("Gender"),
                            ft.RadioGroup(
                                content=ft.Column([
                                    ft.Radio(value="male", label="Male"),
                                    ft.Radio(value="female", label="Female"),
                                    ft.Radio(value="other", label="Other"),
                                ]),
                                on_change=gender_value
                            )
                        ]),
                        ft.TextField(label="Address", on_change=address_value, value=address),
                        ft.Dropdown(
                            label="Select your country",
                            hint_text="Choose a country",
                            width=300,
                            options=[
                                ft.dropdown.Option("AF", "Afghanistan"),
                                ft.dropdown.Option("AL", "Albania"),
                                ft.dropdown.Option("DZ", "Algeria"),
                                ft.dropdown.Option("AD", "Andorra"),
                                ft.dropdown.Option("AO", "Angola"),
                                ft.dropdown.Option("AG", "Antigua and Barbuda"),
                                ft.dropdown.Option("AR", "Argentina"),
                                ft.dropdown.Option("AM", "Armenia"),
                                ft.dropdown.Option("AU", "Australia"),
                                ft.dropdown.Option("AT", "Austria"),
                                ft.dropdown.Option("AZ", "Azerbaijan"),
                                ft.dropdown.Option("BS", "Bahamas"),
                                ft.dropdown.Option("BH", "Bahrain"),
                                ft.dropdown.Option("BD", "Bangladesh"),
                                ft.dropdown.Option("BB", "Barbados"),
                                ft.dropdown.Option("BY", "Belarus"),
                                ft.dropdown.Option("BE", "Belgium"),
                                ft.dropdown.Option("BZ", "Belize"),
                                ft.dropdown.Option("BJ", "Benin"),
                                ft.dropdown.Option("BT", "Bhutan"),
                                ft.dropdown.Option("BO", "Bolivia"),
                                ft.dropdown.Option("BA", "Bosnia and Herzegovina"),
                                ft.dropdown.Option("BW", "Botswana"),
                                ft.dropdown.Option("BR", "Brazil"),
                                ft.dropdown.Option("BN", "Brunei"),
                                ft.dropdown.Option("BG", "Bulgaria"),
                                ft.dropdown.Option("BF", "Burkina Faso"),
                                ft.dropdown.Option("BI", "Burundi"),
                                ft.dropdown.Option("CV", "Cabo Verde"),
                                ft.dropdown.Option("KH", "Cambodia"),
                                ft.dropdown.Option("CM", "Cameroon"),
                                ft.dropdown.Option("CA", "Canada"),
                                ft.dropdown.Option("CF", "Central African Republic"),
                                ft.dropdown.Option("TD", "Chad"),
                                ft.dropdown.Option("CL", "Chile"),
                                ft.dropdown.Option("CN", "China"),
                                ft.dropdown.Option("CO", "Colombia"),
                                ft.dropdown.Option("KM", "Comoros"),
                                ft.dropdown.Option("CD", "Congo, Democratic Republic of the"),
                                ft.dropdown.Option("CG", "Congo, Republic of the"),
                                ft.dropdown.Option("CR", "Costa Rica"),
                                ft.dropdown.Option("CI", "Côte d'Ivoire"),
                                ft.dropdown.Option("HR", "Croatia"),
                                ft.dropdown.Option("CU", "Cuba"),
                                ft.dropdown.Option("CY", "Cyprus"),
                                ft.dropdown.Option("CZ", "Czech Republic"),
                                ft.dropdown.Option("DK", "Denmark"),
                                ft.dropdown.Option("DJ", "Djibouti"),
                                ft.dropdown.Option("DM", "Dominica"),
                                ft.dropdown.Option("DO", "Dominican Republic"),
                                ft.dropdown.Option("EC", "Ecuador"),
                                ft.dropdown.Option("EG", "Egypt"),
                                ft.dropdown.Option("SV", "El Salvador"),
                                ft.dropdown.Option("GQ", "Equatorial Guinea"),
                                ft.dropdown.Option("ER", "Eritrea"),
                                ft.dropdown.Option("EE", "Estonia"),
                                ft.dropdown.Option("SZ", "Eswatini"),
                                ft.dropdown.Option("ET", "Ethiopia"),
                                ft.dropdown.Option("FJ", "Fiji"),
                                ft.dropdown.Option("FI", "Finland"),
                                ft.dropdown.Option("FR", "France"),
                                ft.dropdown.Option("GA", "Gabon"),
                                ft.dropdown.Option("GM", "Gambia"),
                                ft.dropdown.Option("GE", "Georgia"),
                                ft.dropdown.Option("DE", "Germany"),
                                ft.dropdown.Option("GH", "Ghana"),
                                ft.dropdown.Option("GR", "Greece"),
                                ft.dropdown.Option("GD", "Grenada"),
                                ft.dropdown.Option("GT", "Guatemala"),
                                ft.dropdown.Option("GN", "Guinea"),
                                ft.dropdown.Option("GW", "Guinea-Bissau"),
                                ft.dropdown.Option("GY", "Guyana"),
                                ft.dropdown.Option("HT", "Haiti"),
                                ft.dropdown.Option("HN", "Honduras"),
                                ft.dropdown.Option("HU", "Hungary"),
                                ft.dropdown.Option("IS", "Iceland"),
                                ft.dropdown.Option("IN", "India"),
                                ft.dropdown.Option("ID", "Indonesia"),
                                ft.dropdown.Option("IR", "Iran"),
                                ft.dropdown.Option("IQ", "Iraq"),
                                ft.dropdown.Option("IE", "Ireland"),
                                ft.dropdown.Option("IL", "Israel"),
                                ft.dropdown.Option("IT", "Italy"),
                                ft.dropdown.Option("JM", "Jamaica"),
                                ft.dropdown.Option("JP", "Japan"),
                                ft.dropdown.Option("JO", "Jordan"),
                                ft.dropdown.Option("KZ", "Kazakhstan"),
                                ft.dropdown.Option("KE", "Kenya"),
                                ft.dropdown.Option("KI", "Kiribati"),
                                ft.dropdown.Option("KP", "North Korea"),
                                ft.dropdown.Option("KR", "South Korea"),
                                ft.dropdown.Option("KW", "Kuwait"),
                                ft.dropdown.Option("KG", "Kyrgyzstan"),
                                ft.dropdown.Option("LA", "Laos"),
                                ft.dropdown.Option("LV", "Latvia"),
                                ft.dropdown.Option("LB", "Lebanon"),
                                ft.dropdown.Option("LS", "Lesotho"),
                                ft.dropdown.Option("LR", "Liberia"),
                                ft.dropdown.Option("LY", "Libya"),
                                ft.dropdown.Option("LI", "Liechtenstein"),
                                ft.dropdown.Option("LT", "Lithuania"),
                                ft.dropdown.Option("LU", "Luxembourg"),
                                ft.dropdown.Option("MG", "Madagascar"),
                                ft.dropdown.Option("MW", "Malawi"),
                                ft.dropdown.Option("MY", "Malaysia"),
                                ft.dropdown.Option("MV", "Maldives"),
                                ft.dropdown.Option("ML", "Mali"),
                                ft.dropdown.Option("MT", "Malta"),
                                ft.dropdown.Option("MH", "Marshall Islands"),
                                ft.dropdown.Option("MR", "Mauritania"),
                                ft.dropdown.Option("MU", "Mauritius"),
                                ft.dropdown.Option("MX", "Mexico"),
                                ft.dropdown.Option("FM", "Micronesia"),
                                ft.dropdown.Option("MD", "Moldova"),
                                ft.dropdown.Option("MC", "Monaco"),
                                ft.dropdown.Option("MN", "Mongolia"),
                                ft.dropdown.Option("ME", "Montenegro"),
                                ft.dropdown.Option("MA", "Morocco"),
                                ft.dropdown.Option("MZ", "Mozambique"),
                                ft.dropdown.Option("MM", "Myanmar"),
                                ft.dropdown.Option("NA", "Namibia"),
                                ft.dropdown.Option("NR", "Nauru"),
                                ft.dropdown.Option("NP", "Nepal"),
                                ft.dropdown.Option("NL", "Netherlands"),
                                ft.dropdown.Option("NZ", "New Zealand"),
                                ft.dropdown.Option("NI", "Nicaragua"),
                                ft.dropdown.Option("NE", "Niger"),
                                ft.dropdown.Option("NG", "Nigeria"),
                                ft.dropdown.Option("MK", "North Macedonia"),
                                ft.dropdown.Option("NO", "Norway"),
                                ft.dropdown.Option("OM", "Oman"),
                                ft.dropdown.Option("PK", "Pakistan"),
                                ft.dropdown.Option("PW", "Palau"),
                                ft.dropdown.Option("PA", "Panama"),
                                ft.dropdown.Option("PG", "Papua New Guinea"),
                                ft.dropdown.Option("PY", "Paraguay"),
                                ft.dropdown.Option("PE", "Peru"),
                                ft.dropdown.Option("PH", "Philippines"),
                                ft.dropdown.Option("PL", "Poland"),
                                ft.dropdown.Option("PT", "Portugal"),
                                ft.dropdown.Option("QA", "Qatar"),
                                ft.dropdown.Option("RO", "Romania"),
                                ft.dropdown.Option("RU", "Russia"),
                                ft.dropdown.Option("RW", "Rwanda"),
                                ft.dropdown.Option("KN", "Saint Kitts and Nevis"),
                                ft.dropdown.Option("LC", "Saint Lucia"),
                                ft.dropdown.Option("VC", "Saint Vincent and the Grenadines"),
                                ft.dropdown.Option("WS", "Samoa"),
                                ft.dropdown.Option("SM", "San Marino"),
                                ft.dropdown.Option("ST", "Sao Tome and Principe"),
                                ft.dropdown.Option("SA", "Saudi Arabia"),
                                ft.dropdown.Option("SN", "Senegal"),
                                ft.dropdown.Option("RS", "Serbia"),
                                ft.dropdown.Option("SC", "Seychelles"),
                                ft.dropdown.Option("SL", "Sierra Leone"),
                                ft.dropdown.Option("SG", "Singapore"),
                                ft.dropdown.Option("SK", "Slovakia"),
                                ft.dropdown.Option("SI", "Slovenia"),
                                ft.dropdown.Option("SB", "Solomon Islands"),
                                ft.dropdown.Option("SO", "Somalia"),
                                ft.dropdown.Option("ZA", "South Africa"),
                                ft.dropdown.Option("SS", "South Sudan"),
                                ft.dropdown.Option("ES", "Spain"),
                                ft.dropdown.Option("LK", "Sri Lanka"),
                                ft.dropdown.Option("SD", "Sudan"),
                                ft.dropdown.Option("SR", "Suriname"),
                                ft.dropdown.Option("SE", "Sweden"),
                                ft.dropdown.Option("CH", "Switzerland"),
                                ft.dropdown.Option("SY", "Syria"),
                                ft.dropdown.Option("TW", "Taiwan"),
                                ft.dropdown.Option("TJ", "Tajikistan"),
                                ft.dropdown.Option("TZ", "Tanzania"),
                                ft.dropdown.Option("TH", "Thailand"),
                                ft.dropdown.Option("TL", "Timor-Leste"),
                                ft.dropdown.Option("TG", "Togo"),
                                ft.dropdown.Option("TO", "Tonga"),
                                ft.dropdown.Option("TT", "Trinidad and Tobago"),
                                ft.dropdown.Option("TN", "Tunisia"),
                                ft.dropdown.Option("TR", "Turkey"),
                                ft.dropdown.Option("TM", "Turkmenistan"),
                                ft.dropdown.Option("TV", "Tuvalu"),
                                ft.dropdown.Option("UG", "Uganda"),
                                ft.dropdown.Option("UA", "Ukraine"),
                                ft.dropdown.Option("AE", "United Arab Emirates"),
                                ft.dropdown.Option("GB", "United Kingdom"),
                                ft.dropdown.Option("US", "United States"),
                                ft.dropdown.Option("UY", "Uruguay"),
                                ft.dropdown.Option("UZ", "Uzbekistan"),
                                ft.dropdown.Option("VU", "Vanuatu"),
                                ft.dropdown.Option("VA", "Vatican City"),
                                ft.dropdown.Option("VE", "Venezuela"),
                                ft.dropdown.Option("VN", "Vietnam"),
                                ft.dropdown.Option("YE", "Yemen"),
                                ft.dropdown.Option("ZM", "Zambia"),
                                ft.dropdown.Option("ZW", "Zimbabwe"),
                            ],
                            on_change=country_value
                        ),
                        ft.ElevatedButton("Create", on_click=lambda _: page.go("/form/details")),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route=='/form/details':
            page.views.append(
                ft.View(
                    "/form/details",
                    [
                        ft.AppBar(title=ft.Text("Details"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Card(
                            content=ft.Container(
                                ft.Column([
                                    ft.Row([
                                        ft.Text(name),
                                        ft.Text(f"Date of Birth : {birth.strftime("%d-%m-%Y")}")
                                    ],
                                    spacing=30,
                                    ),
                                    ft.Row([
                                        ft.Text(f"Gender : {gender}"),
                                        ft.Text(f"Address : {address}"),
                                    ],
                                    spacing=30,
                                    ),
                                    ft.Row([
                                        ft.Text(f"Country : {country}")
                                    ]),
                                ]),
                                width=400,
                                padding=10,
                            ),
                            shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton("Go back", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    def view_pop(e:ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view:ft.View=page.views[-1]
        page.go(top_view.route)
    
    date_picker.on_change = birth_value
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(
    target=main,
    view=ft.AppView.FLET_APP,
)