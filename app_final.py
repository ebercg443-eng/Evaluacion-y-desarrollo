import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import flet as ft

def main(page: ft.Page):
    page.title = "Business Judgment Estudio Economico y Financiero - Simulador de Evaluación y Desarrollo de Proyectos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ==========================================
    # FUNCIÓN PARA MOSTRAR CRÉDITOS AL CLICKEAR EL ÁGUILA
    # ==========================================
    def mostrar_creditos(e):
        page.snack_bar = ft.SnackBar(
            ft.Text("Creadores: Eber Calderón y Brenda Martínez", color="white", weight=ft.FontWeight.BOLD),
            bgcolor="blue900"
        )
        page.snack_bar.open = True
        page.update()

    # ==========================================
    # ENCABEZADO CON LA PURA ÁGUILA INTERACTIVA
    # ==========================================
    header_banner = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Text("⚡", size=24),
                ft.Text("BUSINESS JUDGMENT", size=22, weight=ft.FontWeight.BOLD, color="white"),
                # El águila interactiva directa
                ft.GestureDetector(
                    content=ft.Text("🦅", size=28),
                    on_tap=mostrar_creditos,
                    tooltip="Autores: Eber Calderon y Brenda Martinez"
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("Estudio Economico y Financiero", size=20, weight=ft.FontWeight.BOLD, color="amber"),
            ft.Text("Ingeniería Electrónica • TecNM • Evaluación y Desarrollo de Proyectos", size=13, color="white70", italic=True),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
        bgcolor="grey900",
        padding=18,
        border_radius=10
    )

    # ==========================================
    # SELECTOR DE TIPO DE PROYECTO
    # ==========================================
    radio_tipo_proyecto = ft.RadioGroup(
        value="social",
        content=ft.Row([
            ft.Radio(value="social", label="Proyecto Social (Evaluación y Desarrollo / E-waste)"),
            ft.Radio(value="inversion", label="Proyecto de Inversión (Lucrativo)"),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # ==========================================
    # CAMPOS DE ENTRADA (PUNTOS 1 AL 8)
    # ==========================================
    txt_costos_fijos = ft.TextField(label="1. Costos Fijos Totales ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_costos_vars = ft.TextField(label="1. Costos Variables Unitarios ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_costos_prod = ft.TextField(label="1. Costos de Producción / Procesamiento ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_costos_oper = ft.TextField(label="1. Costos de Operación ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    txt_sueldos = ft.TextField(label="2.1 Sueldos y Salarios ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_servicios = ft.TextField(label="2.1 Servicios Básicos ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_alquileres = ft.TextField(label="2.1 Alquileres / Sede ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_papeleria = ft.TextField(label="2.1 Papelería y Suministros ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_honorarios = ft.TextField(label="2.1 Honorarios Profesionales ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    
    txt_publicidad = ft.TextField(label="2.2 Publicidad y Promoción / Difusión ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_logistica = ft.TextField(label="2.2 Logística y Distribución ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_servicio_cte = ft.TextField(label="2.2 Atención / Servicio al Beneficiario ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    
    txt_manto_prev = ft.TextField(label="2.3 Mantenimiento Preventivo ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_seguros = ft.TextField(label="2.3 Seguros ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_impuestos = ft.TextField(label="2.3 Impuestos y Licencias ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    txt_activos_fijos = ft.TextField(label="3. Activos Fijos (Maquinaria/Equipo) ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_activos_dif = ft.TextField(label="3. Activos Diferidos ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    txt_activo_circ = ft.TextField(label="4. Activo Circulante ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_pasivo_circ = ft.TextField(label="4. Pasivo Circulante ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_inv_inicial = ft.TextField(label="4. Inventario Inicial ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_colchon_caja = ft.TextField(label="4. Colchón de Caja / Efectivo ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_ctas_cobrar = ft.TextField(label="4. Cuentas por Cobrar ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    txt_proy_ventas = ft.TextField(label="5. Proyección de Unidades / Servicios", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_precio_venta = ft.TextField(label="5. Precio Venta / Cuota Recuperación ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_fondos_verdes = ft.TextField(label="5. Fondos Verdes / Subsidios / Grants ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_costos_financieros = ft.TextField(label="5.3 Costos Financieros ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    txt_tasa_desc = ft.TextField(label="7. Tasa de Descuento (% - Social ref: 12%)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="12")
    txt_inversion_total = ft.TextField(label="7 & 8. Inversión Total del Proyecto ($)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    txt_empleados_dir = ft.TextField(label="9. Empleados / Voluntarios Verdes", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_beneficiarios = ft.TextField(label="9. Personas Beneficiadas Directamente", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_valor_social_est = ft.TextField(label="9. Valor Social/Ambiental Monetizado ($ - SROI)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")
    txt_ewaste_reciclado = ft.TextField(label="9. E-waste / Residuos Reciclados (Kg)", keyboard_type=ft.KeyboardType.NUMBER, filled=True, value="0")

    # ==========================================
    # COMPONENTES DE RESULTADOS
    # ==========================================
    txt_res_tipo = ft.Text("--", size=15, weight=ft.FontWeight.BOLD, color="green")
    txt_res_capital_trabajo = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="purple")
    txt_res_presupuesto_ingresos = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="blue")
    txt_res_presupuesto_egresos = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="red")
    txt_res_punto_eq = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="orange")
    txt_res_estados_fin = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="teal")
    txt_res_razones = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="indigo")
    txt_res_punto_8 = ft.Text("--", size=14, weight=ft.FontWeight.BOLD, color="green")
    txt_res_punto_9 = ft.Text("--", size=13, italic=True, color="black87")

    # ==========================================
    # LÓGICA DE CÁLCULO INTEGRAL
    # ==========================================
    def calcular_estudio(e):
        try:
            tipo = radio_tipo_proyecto.value

            cf = float(txt_costos_fijos.value or 0)
            cv = float(txt_costos_vars.value or 0)
            c_prod = float(txt_costos_prod.value or 0)
            c_oper = float(txt_costos_oper.value or 0)

            g_admin = float(txt_sueldos.value or 0) + float(txt_servicios.value or 0) + float(txt_alquileres.value or 0) + float(txt_papeleria.value or 0) + float(txt_honorarios.value or 0)
            g_ventas = float(txt_publicidad.value or 0) + float(txt_logistica.value or 0) + float(txt_servicio_cte.value or 0)
            g_manto = float(txt_manto_prev.value or 0) + float(txt_seguros.value or 0) + float(txt_impuestos.value or 0)
            total_gastos_operacion = g_admin + g_ventas + g_manto

            act_fijos = float(txt_activos_fijos.value or 0)
            act_dif = float(txt_activos_dif.value or 0)
            inversion_fija_total = act_fijos + act_dif

            act_circ = float(txt_activo_circ.value or 0)
            pas_circ = float(txt_pasivo_circ.value or 0)
            cap_trabajo = act_circ - pas_circ

            unidades = float(txt_proy_ventas.value or 0)
            precio = float(txt_precio_venta.value or 0)
            fondos_v = float(txt_fondos_verdes.value or 0)
            c_fin = float(txt_costos_financieros.value or 0)

            ingresos_totales = (precio * unidades) + fondos_v
            egresos_totales = cf + (cv * unidades) + c_prod + c_oper + total_gastos_operacion + c_fin

            cf_netos = max(0, (cf + c_prod + c_oper + total_gastos_operacion) - fondos_v)
            margen_contribucion = precio - cv
            punto_equilibrio = cf_netos / margen_contribucion if margen_contribucion > 0 else 0
            utilidad_neta = ingresos_totales - egresos_totales

            inv_total = float(txt_inversion_total.value or 0)
            if inv_total <= 0:
                inv_total = inversion_fija_total + cap_trabajo if (inversion_fija_total + cap_trabajo) > 0 else 1

            tasa_desc = float(txt_tasa_desc.value or 0) / 100
            van = (utilidad_neta / (1 + tasa_desc)) - inv_total
            tir = (utilidad_neta / inv_total) * 100

            voluntarios = int(txt_empleados_dir.value or 0)
            beneficiarios = int(txt_beneficiarios.value or 0)
            valor_social = float(txt_valor_social_est.value or 0)
            ewaste = float(txt_ewaste_reciclado.value or 0)

            if tipo == "social":
                txt_res_tipo.value = "DICTAMEN: PROYECTO SOCIAL (Evaluación y Desarrollo / E-waste)"
                txt_res_tipo.color = "green"

                sroi = (valor_social / inv_total) if inv_total > 0 else 0
                costo_por_beneficiario = (egresos_totales / beneficiarios) if beneficiarios > 0 else 0
                cobertura_verde = (fondos_v / egresos_totales * 100) if egresos_totales > 0 else 0
                
                txt_res_punto_8.value = (
                    f"• SROI (Retorno Social): {sroi:.2f}:1 (Por cada $1 se generan ${sroi:.2f} sociales)\n"
                    f"• Costo-Efectividad: ${costo_por_beneficiario:,.2f} por beneficiario\n"
                    f"• Cobertura de Fondos Verdes: {cobertura_verde:.1f}% del gasto operativo\n"
                    f"• Viabilidad Social: {'ACEPTABLE (Sostenible)' if utilidad_neta >= 0 else 'REQUIERE FONDEO'}"
                )

                txt_res_punto_9.value = (
                    f"• Beneficiarios Directos: {beneficiarios:,} personas\n"
                    f"• Capital Humano / Voluntarios: {voluntarios} expertos en electrónica/verde\n"
                    f"• Impacto Ambiental (E-waste): {ewaste:,.2f} Kg de residuos electrónicos reciclados\n"
                    f"• Enfoque: Economía circular y tecnología al servicio de la comunidad."
                )

            else:
                txt_res_tipo.value = "DICTAMEN: PROYECTO DE INVERSIÓN (Lucrativo)"
                txt_res_tipo.color = "blue"

                roi = (utilidad_neta / inv_total) * 100
                margen_neto = (utilidad_neta / ingresos_totales * 100) if ingresos_totales > 0 else 0
                payback = (inv_total / utilidad_neta) if utilidad_neta > 0 else 0
                relacion_bc = (ingresos_totales / egresos_totales) if egresos_totales > 0 else 0

                txt_res_punto_8.value = (
                    f"• ROI (Retorno sobre Inversión): {roi:.2f}%\n"
                    f"• Margen Neto: {margen_neto:.2f}% | Relación B/C: {relacion_bc:.2f}\n"
                    f"• Payback: {payback:.2f} periodos\n"
                    f"• Viabilidad Financiera: {'RENTABLE' if van > 0 else 'NO RENTABLE'}"
                )

                txt_res_punto_9.value = (
                    f"• Empleos Formales: {voluntarios} puestos técnicos\n"
                    f"• Inversión por Puesto: ${(inv_total / voluntarios if voluntarios > 0 else 0):,.2f}\n"
                    f"• RSE (E-waste): {ewaste:,.2f} Kg gestionados\n"
                    f"• Enfoque: Rentabilidad y desarrollo industrial."
                )

            txt_res_capital_trabajo.value = f"Capital de Trabajo Neto: ${cap_trabajo:,.2f} (Activo: ${act_circ:,.2f} - Pasivo: ${pas_circ:,.2f})"
            txt_res_presupuesto_ingresos.value = f"Ingresos Proyectados: ${ingresos_totales:,.2f} (Ventas: ${precio * unidades:,.2f} + Fondos Verdes: ${fondos_v:,.2f})"
            txt_res_presupuesto_egresos.value = f"Egresos Totales: ${egresos_totales:,.2f}"
            txt_res_punto_eq.value = f"Punto de Equilibrio: {punto_equilibrio:,.2f} Unidades / Servicios"
            txt_res_estados_fin.value = f"Flujo Neto / Remanente: ${utilidad_neta:,.2f}"
            txt_res_razones.value = f"TIR: {tir:.2f}% | VAN: ${van:,.2f} | Tasa Desc: {tasa_desc*100:.1f}%"

            page.snack_bar = ft.SnackBar(ft.Text("¡Business Judgment ejecutado con éxito!"), bgcolor="green")
            page.snack_bar.open = True

        except ValueError as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {ex}"), bgcolor="red")
            page.snack_bar.open = True
        
        page.update()

    btn_analizar = ft.Container(
        content=ft.Text("EJECUTAR ANÁLISIS INTEGRAL", color="white", weight=ft.FontWeight.BOLD, size=15),
        bgcolor="green",
        padding=15,
        border_radius=8,
        width=420,
        ink=True,
        on_click=calcular_estudio
    )

    card_diagnostico = ft.Card(
        elevation=4,
        content=ft.Container(
            padding=20,
            width=540,
            content=ft.Column([
                ft.Text("Evaluación de Negocio y Criterio Empresarial", size=16, weight=ft.FontWeight.BOLD, color="green"),
                txt_res_tipo,
                ft.Divider(),
                ft.Text("• 4. Capital de Trabajo:", weight=ft.FontWeight.BOLD, color="grey"),
                txt_res_capital_trabajo,
                ft.Divider(),
                ft.Text("• 5. Presupuestos:", weight=ft.FontWeight.BOLD, color="grey"),
                txt_res_presupuesto_ingresos,
                txt_res_presupuesto_egresos,
                ft.Divider(),
                ft.Text("• 6. Punto de Equilibrio y Estados Financieros:", weight=ft.FontWeight.BOLD, color="grey"),
                txt_res_punto_eq,
                txt_res_estados_fin,
                ft.Divider(),
                ft.Text("• 7. Razones Financieras:", weight=ft.FontWeight.BOLD, color="grey"),
                txt_res_razones,
                ft.Divider(),
                ft.Text("• 8. Indicadores de Rentabilidad / Sostenibilidad:", weight=ft.FontWeight.BOLD, color="grey"),
                txt_res_punto_8,
                ft.Divider(),
                ft.Text("• 9. Indicadores Sociales, Electrónica & E-waste:", weight=ft.FontWeight.BOLD, color="grey"),
                txt_res_punto_9
            ], spacing=8)
        )
    )

    main_content = ft.Container(
        content=ft.Column([
            header_banner,
            ft.Text("Selecciona el enfoque del proyecto:", size=13, color="grey", italic=True),
            radio_tipo_proyecto,
            ft.Divider(height=15),

            ft.Text("1. Estructura de Costos", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_costos_fijos, txt_costos_vars], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_costos_prod, txt_costos_oper], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            ft.Text("2. Gastos de Operación", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_sueldos, txt_servicios], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_alquileres, txt_papeleria], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_honorarios, txt_publicidad], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_logistica, txt_servicio_cte], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_manto_prev, txt_seguros], alignment=ft.MainAxisAlignment.CENTER),
            txt_impuestos,
            ft.Divider(),

            ft.Text("3. Inversión Fija y Derivada", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_activos_fijos, txt_activos_dif], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            ft.Text("4. Capital de Trabajo", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_activo_circ, txt_pasivo_circ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_inv_inicial, txt_colchon_caja], alignment=ft.MainAxisAlignment.CENTER),
            txt_ctas_cobrar,
            ft.Divider(),

            ft.Text("5. Presupuestos y Fondos Verdes", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_proy_ventas, txt_precio_venta], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_fondos_verdes, txt_costos_financieros], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            ft.Text("7 & 8. Parámetros de Evaluación", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_tasa_desc, txt_inversion_total], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            ft.Text("9. Indicadores Sociales, Electrónica & E-waste", size=15, weight=ft.FontWeight.BOLD, color="green"),
            ft.Row([txt_empleados_dir, txt_ewaste_reciclado], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_beneficiarios, txt_valor_social_est], alignment=ft.MainAxisAlignment.CENTER),

            ft.Container(height=15),
            btn_analizar,
            ft.Container(height=15),
            card_diagnostico

        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
        padding=10
    )

    page.add(main_content)

ft.run(main)
