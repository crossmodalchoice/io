function atualizarGoogleSiteComGraficos() {
  // URL do site
  var siteUrl = 'https://sites.google.com/view/crossmodalchoice';
  var site = SitesApp.getSiteByUrl(siteUrl);

  // Nome da página
  var paginaNome = 'Resultados'; 
  var paginaResultados = site.getChildByName(paginaNome);

  if (!paginaResultados) {
    Logger.log('Página "' + paginaNome + '" não encontrada. Verifique o nome.');
    return;
  }

  // IDs dos arquivos no Google Drive
  var idGraficoRadar = '13C2S8mvKIdTo3wZSTUDd9vvR--VzbsMG';
  var idGraficoBarras = '1wOo4Yeg9AsBuH-Ek5lxcZud8SQnAvKie';

  try {
    // Obtém os arquivos do Drive
    var arquivoRadar = DriveApp.getFileById(idGraficoRadar);
    var arquivoBarras = DriveApp.getFileById(idGraficoBarras);

    // Define permissões de visualização
    arquivoRadar.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    arquivoBarras.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);

    // URLs dos gráficos
    var urlGraficoRadar = arquivoRadar.getUrl();
    var urlGraficoBarras = arquivoBarras.getUrl();

    // Atualiza o conteúdo HTML da página
    var html = '<h2>Gráfico Radar</h2>' +
               '<iframe src="' + urlGraficoRadar + '?usp=sharing" width="600" height="400"></iframe>' +
               '<h2>Gráfico de Barras</h2>' +
               '<iframe src="' + urlGraficoBarras + '?usp=sharing" width="600" height="400"></iframe>';

    paginaResultados.setHtmlContent(html);

    Logger.log('Site atualizado com sucesso!');
  } catch (error) {
    Logger.log('Erro ao atualizar o site: ' + error);

    // Tratamento de erro detalhado
    if (error.message.indexOf("Invalid argument: id") > -1) {
      Logger.log("Verifique os IDs dos arquivos no Drive. Podem estar incorretos.");
    } else if (error.message.indexOf("Access denied") > -1) {
      Logger.log("Verifique as permissões dos arquivos no Google Drive.");
    }
  }
}