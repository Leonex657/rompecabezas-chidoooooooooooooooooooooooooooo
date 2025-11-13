import flet as ft

def main(page: ft.Page):
    page.title = "🧩 Rompecabezas: Componentes de la CPU"
    page.bgcolor = ft.Colors.BLUE_50
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    componentes = [
        {
            "titulo": "ALU",
            "funcion": "Realiza operaciones aritméticas y lógicas.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/ALU.png",
        },
        {
            "titulo": "Control",
            "funcion": "Dirige y gestiona las operaciones dentro de la CPU.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/CONTROL.png",
        },
        {
            "titulo": "Registros",
            "funcion": "Almacenan temporalmente datos e instrucciones.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/REGISTROS.png",
        },
        {
            "titulo": "Entrada",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/entrada.png",
        },
        {
            "titulo": "Completo",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/completo1.png",
        },
        
    ]

    resultado = ft.Text(value="", size=18, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    piezas = []

    # --- Función que se ejecuta cuando se suelta una pieza en una zona ---
    def on_accept(e):
        src = page.get_control(e.src_id)
        pieza_nombre = src.data
        destino_nombre = e.control.data

        if pieza_nombre.lower() == destino_nombre.lower():
            # Reemplazar zona con imagen de la pieza
            componente = next(c for c in componentes if c["titulo"] == pieza_nombre)
            e.control.content = ft.Image(
                src=componente["imagen"], width=120, height=80, fit=ft.ImageFit.COVER
            )

            # Desactivar pieza (la ocultamos del área de piezas)
            src.visible = False
            resultado.value = f"✅ ¡Correcto! Has colocado '{pieza_nombre}'."
        else:
            resultado.value = f"❌ '{pieza_nombre}' no pertenece aquí."

        page.update()

    # --- Crear piezas arrastrables ---
    for c in componentes:
        if c["titulo"] != "Completo":
            piezas.append(
                ft.Draggable(
                    group="cpu",
                    data=c["titulo"],
                    content=ft.Container(
                        width=130,
                        height=130,
                        bgcolor=ft.Colors.BLUE_200,
                        border_radius=8,
                        padding=10,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            [
                                ft.Image(src=c["imagen"], width=100, height=60, fit=ft.ImageFit.COVER),
                                ft.Text(c["titulo"], weight=ft.FontWeight.BOLD),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                )
            )

    fondo = ft.Image(
        src=componentes[-1]["imagen"],
        width=800,
        height=500,
        fit=ft.ImageFit.CONTAIN,
    )

    # --- Zonas donde deben colocarse las piezas ---
    zonas = [
        ft.Container(
            left=310,
            top=265,
            width=125,
            height=74,
            content=ft.DragTarget(
                group="cpu",
                data="ALU",
                on_accept=on_accept,
                content=ft.Container(
                    width=125,
                    height=74,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.GREEN),
                    border=ft.border.all(2, ft.Colors.GREEN),
                    border_radius=6,
                ),
            ),
        ),
        ft.Container(
            left=310,
            top=75,
            width=125,
            height=70,
            content=ft.DragTarget(
                group="cpu",
                data="Control",
                on_accept=on_accept,
                content=ft.Container(
                    width=125,
                    height=70,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE),
                    border=ft.border.all(2, ft.Colors.BLUE),
                    border_radius=6,
                ),
            ),
        ),
        ft.Container(
            left=310,
            top=185,
            width=125,
            height=70,
            content=ft.DragTarget(
                group="cpu",
                data="Registros",
                on_accept=on_accept,
                content=ft.Container(
                    width=125,
                    height=70,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.AMBER),
                    border=ft.border.all(2, ft.Colors.AMBER),
                    border_radius=6,
                ),
            ),
        ),
        ft.Container(
            left=106,
            top=280,
            width=80,
            height=60,
            content=ft.DragTarget(
                group="cpu",
                data="Entrada",
                on_accept=on_accept,
                content=ft.Container(
                    width=125,
                    height=45,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.RED),
                    border=ft.border.all(2, ft.Colors.RED),
                    border_radius=6,
                ),
            ),
        ),
        ft.Container(
            left=577,
            top=280,
            width=80,
            height=60,
            content=ft.DragTarget(
                group="cpu",
                data="Salida",
                on_accept=on_accept,
                content=ft.Container(
                    width=125,
                    height=45,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.RED),
                    border=ft.border.all(2, ft.Colors.RED),
                    border_radius=6,
                ),
            ),
        ),
    ]

    # --- Rompecabezas principal ---
    rompecabezas = ft.Stack(
        controls=[fondo] + zonas,
        width=800,
        height=500,
        alignment=ft.alignment.center,
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "💻 Arrastra cada componente de la CPU a su lugar en el diagrama completo:",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(piezas, alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=20),
                rompecabezas,
                ft.Container(height=20),
                resultado,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
