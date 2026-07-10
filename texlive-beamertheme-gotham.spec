%global tl_name beamertheme-gotham
%global tl_revision 78692

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.5.a
Release:	%{tl_revision}.1
Summary:	A modern, minimal-ish, versatile and extendable yet robust theme for Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-gotham
License:	lppl1.3c cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-gotham.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-gotham.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-gotham.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a modern, minimal-ish, versatile, LaTeX3 and
extendable yet robust Beamer theme with some lines of code gathered or
borrowed from other themes. It uses the l3build system to both build and
verify (Test-Driven Development) the delivered code. "Gotham" tries to
bring higher flexibility thanks to LaTeX3 implementation on top of the
good-looking Metropolis theme.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham
%dir %{_datadir}/texmf-dist/source/latex/beamertheme-gotham
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-gotham
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/MANIFEST.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/ctan.ann
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-blueprint.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-dev-impl.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-dev-impl.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-example169transp.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-example169transp.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-example43dark.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-example43dark.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-exampleSimple.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-exampleSimple.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-layout.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-logo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-safetybox.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-user-cmds.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham-user-cmds.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/gotham.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/section-Beamer.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/section-Conclusion.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-gotham/section-Gotham.tex
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-gotham/gotham.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-gotham/gotham.ins
%{_datadir}/texmf-dist/tex/latex/beamertheme-gotham/beamercolorthemegotham.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-gotham/beamerfontthemegotham.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-gotham/beamerinnerthemegotham.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-gotham/beamerouterthemegotham.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-gotham/beamerthemegotham.sty
