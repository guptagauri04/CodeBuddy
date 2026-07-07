from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_title():
    console.print(
        Panel.fit(
            "[bold cyan]🚀 CODEBUDDY[/bold cyan]\n"
            "[italic]Your Personal Coding Companion[/italic]",
            border_style="cyan"
        )
    )


def show_motivation(message):
    console.print(
        Panel(
            f"[yellow]{message}[/yellow]",
            title="💬 Motivation",
            border_style="yellow"
        )
    )


def show_streak(current, longest):
    console.print(
        Panel(
            f"🔥 Current Streak : [bold green]{current}[/bold green]\n\n"
            f"🏆 Longest Streak : [bold cyan]{longest}[/bold cyan]",
            title="📊 Coding Streak",
            border_style="green"
        )
    )


def show_task(task):
    console.print(
        Panel(
            f"[bold white]{task}[/bold white]",
            title="🧠 Today's Coding Task",
            border_style="blue"
        )
    )


def show_goodbye():
    console.print(
        Panel.fit(
            "[bold yellow]👋 Thanks for coding today![/bold yellow]\n"
            "See you tomorrow 🚀",
            border_style="yellow"
        )
    )

def show_main_menu():
    print("\n")
    console.print("[bold magenta]📋 MAIN MENU[/bold magenta]\n")

    console.print("1️⃣  Start Coding")
    console.print("2️⃣  View Statistics")
    console.print("3️⃣  Daily Challenge")
    console.print("4️⃣  Achievements")
    console.print("5️⃣  Settings")
    console.print("6️⃣  Exit\n")

def show_statistics(stats):
    table = Table(
        title="📊 Your Coding Statistics",
        border_style="cyan",
        show_lines=True
    )

    table.add_column("Statistic", style="bold cyan")
    table.add_column("Value", style="bold green", justify="center")

    table.add_row("✅ Tasks Completed", str(stats["tasks_completed"]))
    table.add_row("⏱ Study Minutes", str(stats["study_minutes"]))
    table.add_row("⭐ XP", str(stats["xp"]))
    table.add_row("📈 Level", str(stats["level"]))

    console.print(table)