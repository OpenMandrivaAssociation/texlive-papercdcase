Name:		texlive-papercdcase
Version:	20190228
Release:	1
Summary:	Origami-style folding paper CD case
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/papercdcase
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a LaTeX style file to produce origami-
style folding paper CD cases.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/papercdcase
%doc %{_texmfdistdir}/doc/latex/papercdcase
#- source
%doc %{_texmfdistdir}/source/latex/papercdcase

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
